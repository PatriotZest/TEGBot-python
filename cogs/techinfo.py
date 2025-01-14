from discord.ext import commands
import discord

class techinfo(commands.Cog):
    @commands.command()
    async def cpuz(self, ctx):
        await ctx.send("https://www.cpuid.com/downloads/cpu-z/cpu-z_1.95-en.exe")

    @commands.command()
    async def drivers(self, ctx):
        embed = discord.Embed(title="Drivers", description="Links to downloads for various drivers", color=0x00a0a0)
        embed.add_field(name="AMD Drivers:", value="https://amd.com/en/support", inline=False)
        embed.add_field(name="nVidia Drivers:", value="https://nvidia.com/Download/index.aspx", inline=False)
        embed.add_field(name="Realtek Audio Drivers:", value="https://www.realtek.com/en/downloads", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def hwmonitor(self, ctx):
        await ctx.send("https://www.cpuid.com/downloads/hwmonitor/hwmonitor_1.43.exe")

    @commands.command()
    async def key(self, ctx):
        await ctx.send("https://www.magicaljellybean.com/downloads/KeyFinderInstaller.exe")

    @commands.command()
    async def safemode(self, ctx):
        await ctx.send("https://support.microsoft.com/en-us/windows/start-your-pc-in-safe-mode-in-windows-10-92c27cff-db89-8644-1ce4-b3e5e56fe234")

    @commands.command()
    async def malwarebytes(self, ctx):
        await ctx.send("https://www.malwarebytes.com/mwb-download/thankyou/")

    @commands.command()
    async def windowsinstall(self, ctx):
        await ctx.send("This tutorial will lead you how to do a fresh windows installation: (All your data will be gone, back it up and use `!key` in case you need to back up your Product Key too, please save it somewhere safe and don't show us or anyone the key!)\nhttps://youtu.be/bwJ_E-I9WRs\nTo figure out which key you need to use to boot to a usb, run the command `!bootkeys`.")

    @commands.command()
    async def bootkeys(self, ctx):
        embed = discord.Embed(title="", description="", color=0x00a0a0)
        embed.add_field(name="Dell, Toshiba, Huawei, Lenovo:", value="F12", inline=True)
        embed.add_field(name="Acer:", value="F12, F9, F2, Esc", inline=True)
        embed.add_field(name="Apple:", value="Option / Alt", inline=True)
        embed.add_field(name="Asus:", value="Esc", inline=True)
        embed.add_field(name="HP:", value="F9", inline=True)
        embed.add_field(name="Intel:", value="F10", inline=True)
        embed.add_field(name="MSI:", value="F11", inline=True)
        embed.add_field(name="Samsung:", value="Esc, F12, F2", inline=True)
        embed.add_field(name="Sony:", value="Esc, F10, F11", inline=True)
        embed.add_field(name="Other Common Ones:", value="F2, F10, F12, Esc, Del", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def linuxusb(self, ctx):
        embed = discord.Embed(title="How to get a Linux Live USB", color=0x00a0a0)
        embed.add_field(name="Step 1:", value="Decide what distro is best for you.\nIf you're not experienced with computers go with Linux Mint.\nIf you're experienced with computers but not with Linux go for Fedora or Manjaro.\nTry Fedora if you want something with a sleek modern design, or Manjaro's XFCE version if you want a more familiar design.", inline=False)
        embed.add_field(name="Step 2:", value="Download the Linux ISO and the flashing tool.\nDepending on what distro you chose pick one of these links:\nLinux Mint: https://linuxmint.com/download.php\nManjaro XFCE: https://manjaro.org/downloads/official/xfce/\nFedora: https://getfedora.org/en/workstation/download/ (Instead of Fedora Media Writer, make sure to download the x86_64 ISO)\nFor the flashing tool you can use balenaEtcher or Rufus.\nbalenaEtcher is simple and gets the job done fast: https://balena.io/etcher/\nRufus has many more features but can be confusing to novices: https://rufus.ie", inline=False)
        embed.add_field(name="Step 3:", value="Once everything is downloaded, use the flashing tool to flash your ISO to a USB (the usb must be 8 GB or larger).\nSelect the Linux ISO you downloaded and the USB you want to flash to, then start the flashing process.\nWhen the flashing is done, unplug the usb and plug it into the device you want to boot into Linux (if it's the same device just leave it plugged in and shut down the PC).", inline=False)
        embed.add_field(name="Step 4:", value="Boot into Linux.\nTurn on the computer and start spamming the boot menu key (figure out which one yours is with the `!bootkey` command) until the menu pops up.\nWhen the menu pops up, select the USB to boot to.", inline=False)
        embed.add_field(name="Step 5:", value="Install or try out linux.\nYour computer will boot to show the Linux desktop. Note that Linux is not installed on the computer, it's what is called a Live USB where you can test it out before you try it. Anything you do on the USB in this state will not be saved and doesn't affect your PC. If you wish to replace Windows with Linux, open the 'Install Linux' file on the desktop. If you want to return to Windows on the next reboot, simply restart the PC with the USB unplugged.", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(techinfo(bot))
