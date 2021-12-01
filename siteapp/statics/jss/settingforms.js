function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csr = getCookie("csrftoken")


var changepass = "<input type='password' class='oldpass' name='oldpass' placeholder='Password'><input class='newpass' type='password' name='newpass' placeholder='New Password'><input class='confirmpass' type='password' name='confirmpass' placeholder='Confirm Password'><input class='submit' type='submit' value='Change Password'>"

var logout = "<input class='logout-submit' type='submit'>"


var delacount = "<input type='password' class='password' name='password' placeholder='Acount Password'><input class='submit-del' type='submit' value='Delete Acount'>"
