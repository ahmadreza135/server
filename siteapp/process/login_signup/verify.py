import smtplib,ssl
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.shortcuts import render
from siteapp.models import dashboard as User
import django,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from serapp.models import emailv



verification_code = {}
veri_codes = {}

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
        global verif_codes
        global verification_code

    def first(request):
        # print(request.user)
        if "first_req" in request.POST and "email" in request.POST:
            req_email = request.POST.get("email")
            try:
                u = User.objects.get(username=req_email)
                if u is not None:
                    # u.delete()
                    return {"email_exixt":"true"}
                else:
                    return{"isnone":"yes"}    
            except django.contrib.auth.models.User.DoesNotExist: 
                # TODO : send verification email to email
                print('ok')
                verification_code[req_email] = random.randint(random.randint(100000,150000),random.randint(900000,990000))
                if verify_email.send_email(request.POST.get("email"),"This Is Your Verification Code For My Application\n"+str(verification_code[req_email])):
                    print(verification_code[req_email])
                    return render(request,"../templates/verify_second.html",{"email":req_email})
                else:
                    return {"email_exist":"false"}    
        else:
            {"wrong_req":"true"}        
    def second(request):
        if "verification_code" in request.POST:
            requ_email = request.POST.get("email")
            try:
                if str(verification_code[requ_email]) == request.POST.get("verification_code"):
                    verification_code.pop(requ_email)
                    

                    vers = emailv.objects.get(email=requ_email)
                    print("yes")
                    # emailv.objects.delete(email=requ_email)
                    if vers is not None:
                        return {"respons":"false"} # TODO : save this response to database

                else:
                    return {"res":"wrong code"}
            except KeyError:
                return {"verify_email_sent":"False"}
                print("no")
            except emailv.DoesNotExist:
                Email = request.POST['email']
                NewPassword = request.POST['newpassword']
                em = emailv(email=requ_email)
                em.save()
                u = User.objects.create_user(username=requ_email)
                u.set_password(NewPassword)
                u.last_name = "false"
                u.save()
                return render(request,"../templates/dashboard.html",{})
    def forget_password(request):
        email = request.POST['email']
        try:
            if "veri_code" in request.POST:
                code = request.POST['veri_code']
                if code == str(veri_codes[email]):
                    u = User.objects.get(username=email)
                    generate_password = User.objects.make_random_password()
                    u.set_password(generate_password)
                    u.save()
                    if verify_email.send_email(email,"This Is Your Generated Password For My Application\n" + generate_password):
                        d = {"sent":"true"}
                    else:
                        d = {"sent":"false"}

            else:            
                veri_codes[email] = random.randint(random.randint(100000,150000),random.randint(900000,990000))
                veri_code = veri_codes[email]
                if verify_email.send_email(email,"This Is Your Verification Code For My Application\n" + str(veri_code)):
                    d = {"sent":"true"}
                else:
                    d = {"sent":"false"}    
        except User.DoesNotExist:
            d = {"user_exist":"false"}
        return d