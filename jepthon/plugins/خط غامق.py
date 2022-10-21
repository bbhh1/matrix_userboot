# DaR
# © matrix Team 2023
# ها شعدك داخل ع الملف تريد تخمط ؟ ابو زربة لهل درجة فاشل  
from telethon import events
from jepthon import jepiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions

@jepiq.on(admin_cmd(pattern="خط غامق"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل الخط الغامق بنجاح ✓**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**᯽︙ تم اطفاء الخط الغامق بنجاح ✓ **")
        return

@jepiq.on(events.NewMessage(outgoing=True))
async def reda(event):
    isbold = gvarstatus("bold")
    if isbold:
        await event.edit(f"**{event.message.message}**")
