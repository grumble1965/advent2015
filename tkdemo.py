import asyncio
import aiohttp
from datetime import datetime, timedelta
from pynws import SimpleNWS, NwsError
from textwrap import TextWrapper
from tkinter import *
from tkinter.font import Font
from tkinter import ttk

LOCATION = (48.1829, -117.0607)
STATION = 'ITDA8'   # Old Town
USERID = "kmhall@gmail.com"
xMax = 80
REFRESH_RATE = 5 * 60 * 1000        # 5 minutes

nws = None
myWrap = None

root = None
statusContents = None
forecastText = None


def getWindDirection(windDirection):
    if (windDirection > 315.0+1.0):
        return "NNW"
    if (windDirection > 292.5+1.0):
        return "NW"
    if (windDirection > 270.0+1.0):
        return "WNW"
    if (windDirection > 247.5+1.0):
        return "W"
    if (windDirection > 225.0+1.0):
        return "WSW"
    if (windDirection > 202.5+1.0):
        return "SW"
    if (windDirection > 180.0+1.0):
        return "SSW"
    if (windDirection > 157.5+1.0):
        return "S"
    if (windDirection > 135.0+1.0):
        return "SSE"
    if (windDirection > 112.5+1.0):
        return "SE"
    if (windDirection > 90.0+1.0):
        return "ESE"
    if (windDirection > 67.5+1.0):
        return "E"
    if (windDirection > 45.0+1.0):
        return "ENE"
    if (windDirection > 22.5+1.0):
        return "NE"
    if (windDirection > 0.0+1.0):
        return "NNE"
    return "N"


def decorateForecast():
    # set up tags
    for tag in forecastText.tag_names():
        forecastText.tag_delete(tag)

    myfont = Font(font=forecastText['font']).copy()
    myfont.configure(weight='bold')
    forecastText.tag_configure(
        'boldline', font=myfont, foreground='white', background='blue')
    forecastText.tag_configure(
        'alertline', font=myfont, foreground='white', background='red')

    # bold tag for Observation: and Forecast:
    loc = '1.0'
    idxStart = forecastText.search('Observation:', loc)
    if idxStart != '':
        idxEnd = idxStart + " wordend"
        forecastText.tag_add('boldline', idxStart, idxEnd)

    # bold tag for Forecast:
    loc = '1.0'
    idxStart = forecastText.search('Forecast:', loc)
    if idxStart != '':
        idxEnd = idxStart + " wordend"
        forecastText.tag_add('boldline', idxStart, idxEnd)

    # alert tag for Alert:
    loc = '1.0'
    idxStart = forecastText.search('Alert:', loc)
    if idxStart != '':
        idxEnd = idxStart + " wordend"
        forecastText.tag_add('alertline', idxStart, idxEnd)


def observationToText(obs):
    obs_time = datetime.fromisoformat(obs['timestamp']).astimezone()
    obs_temp = 9 * obs['temperature'] / 5.0 + 32.0
    obs_speed = obs['windSpeed'] * 0.6213712
    obs_direction = getWindDirection(obs['windDirection'])

    obs_gust = None
    if obs['windGust']:
        obs_gust = obs['windGust'] * 0.6213712

    obs_humidity = obs['relativeHumidity']
    lastFetch = datetime.now()

    line = "Observation:  "
    line += f"{obs_time.strftime('%A %I:%M%p')}  "
    line += f"Fetched {lastFetch.strftime('%I:%M%p')}"
    line += '\n'

    line += f"  Temp: {obs_temp:.1f} F  "
    line += f"Humidity: {obs_humidity:.0f}  %"
    line += f"  Wind: {obs_direction} {obs_speed:.1f} mph"
    if obs_gust:
        line += ", gusts to {obs_gust:.1f} mph"
    line += '\n'

    return line


def forecastToText(fc):
    fc_start = datetime.fromisoformat(fc['startTime']).astimezone()
    fc_end = datetime.fromisoformat(fc['endTime']).astimezone()
    fc_name = fc['name']
    fc_shorttext = fc['shortForecast']
    fc_detailed = fc['detailedForecast']

    line = ""
    if fc_start.day == fc_end.day:
        line += f"  From {fc_start.strftime('%A %I:%M%p')} to {fc_end.strftime('%I:%M%p')}"
    else:
        line += f"  From {fc_start.strftime('%A %I:%M%p')} to {fc_end.strftime('%A %I:%M%p')}"
    line += '\n'

    line += f"  {fc_name}:  {fc_shorttext}  "
    line += '\n'

    for ll in myWrap.wrap(fc_detailed):
        if ll:
            line += '     ' + f"{ll.strip()}"
        line += '\n'
    return line


def alertToText(alert):
    line = ""
    if alert:
        line += "Alerts:\n"
        for stmt in alert:
            msg = stmt['messageType']
            event = stmt['event']
            start = datetime.fromisoformat(stmt['effective']).astimezone()
            stop = datetime.fromisoformat(stmt['expires']).astimezone()
            line += f"     {msg}: {event}" + " "*20
            if start.day == stop.day:
                line += f"({start.strftime('%A %I:%M%p')} to {stop.strftime('%I:%M%p')})"
            else:
                line += f"({start.strftime('%A %I:%M%p')} to {stop.strftime('%A %I:%M%p')})"
            line += '\n'
            headline = stmt['parameters']['NWSheadline']
            for hl in myWrap.wrap("".join(headline)):
                line += f"     {hl}\n"
            line += '\n'
    else:
        line += "No Alerts\n"

    return line


def getNwsText():
    global nws
    tt = "No forecast available..."

    if nws is not None:
        tt = ""
        tt += observationToText(nws.observation) + "\n"

        tt += "Forecast:  \n"
        for ff in nws.forecast[0:2]:
            tt += forecastToText(ff) + "\n"

        tt += alertToText(nws.alerts_forecast_zone) + "\n"

    return tt


async def fetchNws():
    global nws, forecastText, statusContents, root
    statusContents.set('Fetching forecast...')
    try:
        async with aiohttp.ClientSession() as session:
            nws = SimpleNWS(*LOCATION, USERID, session)
            await nws.set_station(STATION)
            await nws.update_observation()
            await nws.update_forecast()
            await nws.update_alerts_forecast_zone()
        forecastText.delete('1.0', 'end')
        forecastText.insert('end', getNwsText())
        decorateForecast()
        statusContents.set('Complete!')
    except Exception as e:
        statusContents.set('Error')
        forecastText.delete('1.0', 'end')
        forecastText.insert('1.0', e)


def getNwsForecast(*args):
    global root
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetchNws())
    except Exception as e:
        print(f"Exception: {e}")
    root.after(REFRESH_RATE, getNwsForecast)


def main():
    global statusContents, forecastText, nws, myWrap, root

    myWrap = TextWrapper(width=xMax - 10)

    root = Tk()
    root.title("Demo NWS")
    frm = ttk.Frame(root, padding='10 10 10 10')
    frm.grid()

    statusContents = StringVar()

    statusLabel = ttk.Label(frm, textvariable=statusContents)
    statusLabel.grid(column=0, row=0)
    statusContents.set('Hello, World!')

    quitButton1 = ttk.Button(frm, text="Quit", command=root.destroy)
    quitButton1.grid(column=2, row=0)

    nwsButton = ttk.Button(frm, text="NWS", command=getNwsForecast)
    nwsButton.grid(column=1, row=0)

    forecastText = Text(frm, width=85, height=20,
                        wrap='none', fg='white', bg='black', font='LucidaConsole')
    ys = ttk.Scrollbar(frm, orient='vertical', command=forecastText.yview)
    forecastText.grid(column=0, row=1, columnspan=3, sticky='nwse')
    forecastText['state'] = 'normal'
    forecastText['yscrollcommand'] = ys.set
    ys.grid(column=3, row=1, sticky='nse')

    # after 5 seconds for the window to be established, fetch the NWS info
    root.after(5000, getNwsForecast)
    root.mainloop()


if __name__ == '__main__':
    main()
