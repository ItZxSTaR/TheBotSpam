import glob
import sys
import asyncio
import logging
import importlib

from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


def load_plugins(plugin_name):
    path = Path(f"AltBots/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"AltBots.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["AltBots.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)


files = glob.glob("AltBots/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝐗𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @𝐏𝐲𝐗𝐞𝐧")


async def main():
    if X1:
        await X1.run_until_disconnected()
    if X2:
        await X2.run_until_disconnected()
    if X3:
        await X3.run_until_disconnected()
    if X4:
        await X4.run_until_disconnected()
    if X5:
        await X5.run_until_disconnected()
    if X6:
        await X6.run_until_disconnected()
    if X7:
        await X7.run_until_disconnected()
    if X8:
        await X8.run_until_disconnected()
    if X9:
        await X9.run_until_disconnected()
    if X10:
        await X10.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
