import smtplib,ssl
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.shortcuts import render
# from siteapp.models import dashboard as User
import django,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from serapp.models import emailv
from django.shortcuts import redirect
from siteapp.models import dashboard
from django.shortcuts import render


verification_code = {}
veri_codes = {}
special_codes = {}

class verify_email:
    sender_address = 'rdaqasmy811@gmail.com'
    sender_pass = 'Rezasm8511'
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    global sender_email
    sender_email = sender_address
    password = sender_pass

    context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    global server
    # try:
    #     a = server
    #     print("yes none")
    # except NameError:
    #     print("no not")
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)

    def send_email(receiver_email, message):
        messages = MIMEMultipart()
        messages['From'] = sender_email
        messages['To'] = receiver_email
        messages['Subject'] = 'This Is From softcoin' 
        messages.attach(MIMEText(message, 'plain'))
        text = messages.as_string()
        try:
            server.sendmail(sender_email, receiver_email,text)
            return True
        except smtplib.SMTPRecipientsRefused:
            return False 
        except smtplib.SMTPServerDisconnected:
            return False
        global verif_codes
        global verification_code

    def first(request):
        data = {}
        if request.method == "POST":
            # print(request.user)
            if "email" in request.POST:
                req_email = request.POST.get("email")
                try:
                    u = dashboard.objects.get(username=req_email)
                    if u is not None:
                        # u.delete()
                        data = {"error":"user exist"}
                    else:
                        data = {"error":"isnone"}    
                except dashboard.DoesNotExist: 
                    # TODO : send verification email to email
                    verification_code[req_email] = random.randint(random.randint(100000,150000),random.randint(900000,990000))
                    if verify_email.send_email(request.POST.get("email"),"This Is Your Verification Code For My Application\n"+str(verification_code[req_email])):
                        print(verification_code[req_email])
                        return render(request,"sign_up/verify_second.html",{"email":req_email})
                    else:
                        data = {"error":"email is worng"}    
            else:
                data = {"error":"wrong_request reload page and try again"}
            request.session["error_data"] = data    
        else:
            context = request.session["error_data"]
            request.session.pop("error_data")
            return render(request,"sign_up/verify_second.html",context = context)
        return redirect("/acount/sign_up/")
    def second(request):
        data = {}
        if request.method == "POST":
            if "verification_code" in request.POST:
                requ_email = request.POST.get("email")
                try:
                    if str(verification_code[requ_email]) == request.POST.get("verification_code"):
                        verification_code.pop(requ_email)

                        vers = emailv.objects.get(email=requ_email)
                        # emailv.objects.delete(email=requ_email)
                        if vers is not None:
                            data = {"error":"user_exist"}# TODO : save this response to database

                    else:
                        data = {"error":"wrong_verify_code"}
                except KeyError:
                    data = {"error":"verify_code_not_get"}
                    
                except emailv.DoesNotExist:
                    Email = request.POST['email']
                    NewPassword = request.POST['newpassword']
                    cpass = request.POST["confirmpass"]
                    if cpass == NewPassword:
                        em = emailv(email=requ_email)
                        em.save()
                        u = dashboard.objects.create_user(username=requ_email)
                        u.set_password(NewPassword)
                        u.last_name = "false"
                        u.save()
                        request.session['_old_post'] = request.POST
                        request.session["_old_post"]["username"] = requ_email
                        request.session["_old_post"]["password"] = NewPassword
                        return redirect("/acount/dashboard/")
                    else:
                        data = {"error":"confirm password is not password"}
            else:
                data = {"error":"wrong request"}
        request.session["error_data"] = data   
        return redirect("/acount/send_code/") 
    def forget_password(request):
        if request.method == "POST":
            r = request.POST
            email = r['email']
            try:
                if "veri_code" in r:
                    code = request.POST['veri_code']
                    if code == str(veri_codes[email]):
                        special_codes[email] = str(random.randint(random.randint(1000000,1500000),random.randint(9000000,9900000))) + dashboard.objects.make_random_password()
                        d = render(request,"sign_up/set_pass.html",{"email":email,"special_code":special_codes[email]})
                elif "email" in r and "special_code" in r and "password" in r and "confirmpass" in r:
                    print(type(r["special_code"]),type(special_codes[email]))
                    if r["special_code"] == special_codes[email] and r["password"] == r["confirmpass"]:
                        us = dashboard.objects.get(username=email)
                        us.set_password(r["password"])
                        us.save()
                        d = redirect("/acount/login/")
                else:            
                    veri_codes[email] = random.randint(random.randint(100000,150000),random.randint(900000,990000))
                    veri_code = veri_codes[email]
                    print(veri_code)
                    if verify_email.send_email(email,"This Is Your Verification Code For My Application\n" + str(veri_code)):
                        d = render(request, "sign_up/enter_ver_code.html", {"email":email})
                        
                    else:
                        d = {"sent":"false"}    
            except dashboard.DoesNotExist:
                d = {"user_exist":"false"}
            return d
        else:
            return render(request,"sign_up/forget.html",{})