import smtplib,ssl
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.contrib.auth.models import User
import django,random

from serapp.models import emailv



verification_code = {}

class verify_email:
    sender_address = 'rdaqasmy811@gmail.com'
    sender_pass = 'Rezasm8511'
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    global sender_email
    sender_email = sender_address
    password = sender_pass
    context = ssl.create_default_context()
    global server
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)


    def send_email(receiver_email, message):
        server.sendmail(sender_email, receiver_email, message)
        global verif_codes
        global verification_code

    def first(request):
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
                verification_code[req_email] = random.randint(random.randint(100000,150000),random.randint(900000,990000))
                verify_email.send_email(request.POST.get("email"),"This Is Your Verification Code For My Application\n"+str(verification_code[req_email]))
                print(verification_code[req_email])
                return {"code_sent":"true"}

    def second(request):
        if "verification_code" in request.POST and "email" in request.POST:
            requ_email = request.POST.get("email")
            try:
                if str(verification_code[requ_email]) == request.POST.get("verification_code"):
                    verification_code.pop(requ_email)

                    vers = emailv.objects.get(email=requ_email)
                    if vers is not None:
    
                    return {"respons":"false"} # TODO : save this response to database

                else:
                    return {"res":"wrong code"}
            except KeyError:
                return {"verify_email_sent":"False"}
            except emailv.DoesNotExist:
                Email = request.POST['email']
                NewPassword = request.POST['newpassword']
                em = emailv(email=requ_email)
                em.save()
                u = User.objects.create_user(username=requ_email)
                u.set_password(NewPassword)
                u.last_name = "false"
                u.save()
                return {"sign_uped":"true"}
