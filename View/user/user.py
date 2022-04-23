import bs4
import requests
from django.shortcuts import render, redirect

from Model.sqlitedao import SqliteDao
from Model.user.userdao.userdao import UserDAO
from Model.user.uservo.uservo import UserVO


############ 회원가입, 로그인, 비밀번호 찾기 ############
sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
userdao = UserDAO('shop');

def register(request):

    return render(request, 'user/register.html')

def registerok(request):

    return render(request, 'user/registerok.html')

def registerimpl(request):

    try:
        email = request.POST['inputEmail'];
        pwd = request.POST['inputPassword'];
        pwd_confirm = request.POST['inputPasswordConfirm'];
        fname = request.POST['inputFirstName'];
        lname = request.POST['inputLastName'];
        name = fname + lname

        # loginuser = userdao.insert(email);
        # if email == loginuser.getEmail():
        #     print('이메일 중복')

        request.session['sessionemail'] = email
        request.session['sessionpwd'] = pwd
        request.session['sessionpwd_confirm'] = pwd_confirm
        request.session['sessionfname'] = fname
        request.session['sessionlname'] = lname

        if email == '':
            print('이메일을 입력하세요')
            context = {
                'center': 'user/failtext/registeremailfail.html'
            }
            return render(request, 'user/return/rregister.html', context);

        if pwd == '':
            print('비밀번호 입력하세요')
            context = {
                'center': 'user/failtext/registerpwdfail.html'
            }
            return render(request, 'user/return/rregister.html', context);

        if pwd_confirm == '':
            print('비밀번호 입력하세요')
            context = {
                'center': 'user/failtext/registerpwdfail.html'
            }
            return render(request, 'user/return/rregister.html', context);

        if pwd != pwd_confirm:
            print('비밀번호 불일치')
            context = {
                'center' : 'user/failtext/registerpwdfail2.html'
            }
            return render(request, 'user/return/rregister.html', context);

        if fname == '':
            print('성을 입력하세요')
            context = {
                'center': 'user/failtext/fnamefail.html'
            }
            return render(request, 'user/return/rregister.html', context);

        if lname == '':
            print('이름을 입력하세요')
            context = {
                'center': 'user/failtext/lnamefail.html'
            }
            return render(request, 'user/return/rregister.html', context);

        else:
            user = UserVO(email, pwd, name);

            userdao.insert(user);
            context = {
                'rname': name
            };

            return render(request, 'user/registerok.html', context);
    except:
        print('중복 이메일')
        context = {
            'center': 'user/failtext/loginemailfail2.html'
        }
        return render(request, 'user/return/rregister.html', context);

def registerdel(request):

    return render(request, 'user/registerdel.html');

def registerdelimpl(request):

    try:
        email = request.POST['inputEmail'];
        pwd = request.POST['inputPassword'];
        fname = request.POST['inputFirstName'];
        lname = request.POST['inputLastName'];
        name = fname + lname

        request.session['sessionemail'] = email
        request.session['sessionpwd'] = pwd
        request.session['sessionfname'] = fname
        request.session['sessionlname'] = lname

        if email == '':
            print('이메일 비입력')
            context = {
                'center': 'user/failtext/registeremailfail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        if pwd == '':
            print('비밀번호 비입력')
            context = {
                'center': 'user/failtext/registerpwdfail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        if fname == '':
            print('성 비입력')
            context = {
                'center': 'user/failtext/fnamefail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        if lname == '':
            print('이름 비입력')
            context = {
                'center': 'user/failtext/lnamefail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        deluser = userdao.select(email);
        if email != deluser.getEmail():
            print('이메일 불일치')
            context = {
                'center': 'user/failtext/delfail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        if pwd != deluser.getPwd():
            print('비밀번호 불일치')
            context = {
                'center': 'user/failtext/delfail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        if name != deluser.getName():
            print('성명 불일치')
            context = {
                'center': 'user/failtext/delfail.html'
            }
            return render(request, 'user/return/rregisterdel.html', context);

        else:
            user = UserVO(email, pwd, name);

            userdao.delete(user);
            context = {
                'rname': name
            };
            del request.session['sessionid'];
            return render(request, 'user/registerdelok.html', context);

    except:
        print('이메일 불일치')
        context = {
            'center': 'user/failtext/delfail.html'
        }
        return render(request, 'user/return/rregisterdel.html', context);

def login(request):

    return render(request, 'user/login.html')

def logout(request):

    if request.session['sessionid'] != '':
        del request.session['sessionid'];

    return redirect('index')

def loginimpl(request):
    remember = request.POST['inputRemember'];

    if remember == 'Rememberdel':
        try:
            email = request.POST['inputEmail'];
            pwd = request.POST['inputPassword'];

            print(email, pwd)
            print(remember)
            request.session['sessionremember'] = remember
            request.session['sessionemail'] = email
            request.session['sessionpwd'] = pwd
            del request.session['sessionremember']

            if email == '':
                print('이메일을 입력하세요')
                context = {
                    'center': 'user/failtext/loginemailfail.html'
                }
                return render(request, 'user/return/rlogin.html', context);

            if pwd == '':
                print('비밀번호를 입력하세요')
                context = {
                    'center': 'user/failtext/loginpwdfail.html'
                }
                return render(request, 'user/return/rlogin.html', context);

            loginuser = userdao.select(email);
            UserVO.print(loginuser)
            userlist = []
            userlist.append(UserVO.print(loginuser));
            print(userlist[0][2])

            if pwd != loginuser.getPwd():
                print('비밀번호 불일치')
                context = {
                    'center': 'user/failtext/loginpwdfail2.html'
                }
                return render(request, 'user/return/rlogin.html', context);

            if pwd == loginuser.getPwd():
                request.session['sessionid'] = userlist[0][2]+'님';

                return redirect('index')

        except Exception as e:
            print('중복 이메일',e)
            context = {
                'center': 'user/failtext/loginemailfail2.html'
            }
            return render(request, 'user/return/rlogin.html', context);
    else:
        try:
            email = request.POST['inputEmail'];
            pwd = request.POST['inputPassword'];

            print(email, pwd)
            print(remember)
            request.session['sessionremember'] = remember
            request.session['sessionemail'] = email
            request.session['sessionpwd'] = pwd

            if email == '':
                print('이메일을 입력하세요')
                context = {
                    'center': 'user/failtext/loginemailfail.html'
                }
                return render(request, 'user/return/rlogin.html', context);

            if pwd == '':
                print('비밀번호를 입력하세요')
                context = {
                    'center': 'user/failtext/loginpwdfail.html'
                }
                return render(request, 'user/return/rlogin.html', context);

            loginuser = userdao.select(email);
            UserVO.print(loginuser)
            userlist = []
            userlist.append(UserVO.print(loginuser));
            print(userlist[0][2])

            if pwd != loginuser.getPwd():
                print('비밀번호 불일치')
                context = {
                    'center': 'user/failtext/loginpwdfail2.html'
                }
                return render(request, 'user/return/rlogin.html', context);

            if pwd == loginuser.getPwd():
                request.session['sessionid'] = userlist[0][2] + '님';

                return redirect('index')

        except Exception as e:
            print('중복 이메일', e)
            context = {
                'center': 'user/failtext/loginemailfail2.html'
            }
            return render(request, 'user/return/rlogin.html', context);

def update(request):

    return render(request, 'user/update.html')

def updateimpl(request):

    email = request.session['sessionemail'];
    pwd = request.POST['inputPassword'];
    pwd_confirm = request.POST['inputPasswordConfirm'];
    fname = request.POST['inputFirstName'];
    lname = request.POST['inputLastName'];
    name = fname + lname
    print('정보 입력 됨')
    # loginuser = userdao.insert(email);
    # if email == loginuser.getEmail():
    #     print('이메일 중복')

    request.session['sessionemail'] = email
    request.session['sessionpwd'] = pwd
    request.session['sessionpwd_confirm'] = pwd_confirm
    request.session['sessionfname'] = fname
    request.session['sessionlname'] = lname

    if pwd == '':
        print('비밀번호 입력하세요')
        context = {
            'center': 'user/failtext/updatefail.html'
        }
        return render(request, 'user/return/rupdate.html', context);

    if pwd_confirm == '':
        print('비밀번호 입력하세요')
        context = {
            'center': 'user/failtext/updatefail.html'
        }
        return render(request, 'user/return/rupdate.html', context);

    if fname == '':
        print('성을 입력하세요')
        context = {
            'center': 'user/failtext/fnamefail.html'
        }
        return render(request, 'user/return/rupdate.html', context);

    if lname == '':
        print('이름을 입력하세요')
        context = {
            'center': 'user/failtext/lnamefail.html'
        }
        return render(request, 'user/return/rupdate.html', context);

    if pwd != pwd_confirm:
        print('비밀번호 불일치')
        context = {
            'center': 'user/failtext/updatefail2.html'
        }
        return render(request, 'user/return/rupdate.html', context);

    else:
        user = UserVO(email, pwd, name);
        userdao.update(user);
        context = {
            'rname': name
        };
        print('업데이트 성공')
        request.session['sessionid'] = name + '님'
        return render(request, 'user/updateok.html', context);

def password(request):

    return render(request, 'user/password.html')

def passwordimpl(request):

    try:
        email = request.POST['inputEmail'];
        fname = request.POST['inputFirstName'];
        lname = request.POST['inputLastName'];

        request.session['sessionemail'] = email
        request.session['sessionfname'] = fname
        request.session['sessionlname'] = lname

        print(email, fname, lname)
        if email == '':
            print('이메일을 입력하세요')
            context = {
                'center': 'user/failtext/loginemailfail.html'
                }
            return render(request, 'user/return/rpassword.html', context);

        if fname == '':
            print('성 비입력')
            context = {
                'center': 'user/failtext/fnamefail.html'
                }
            return render(request, 'user/return/rpassword.html', context);

        if lname == '':
            print('이름 비입력')
            context = {
                'center': 'user/failtext/lnamefail.html'
                }
            return render(request, 'user/return/rpassword.html', context);

        deluser = userdao.select(email);
        name = fname + lname
        if email != deluser.getEmail():
            print('이메일 불일치')
            context = {
                'center': 'user/failtext/delfail.html'
                }
            return render(request, 'user/return/rpassword.html', context);

        if name != deluser.getName():
            print('성명 불일치')
            context = {
                'center': 'user/failtext/delfail.html'
                }
            return render(request, 'user/return/rpassword.html', context);

        else:
            return render(request, 'user/changepassword.html');

    except:
        print('중복 이메일')
        context = {
            'center': 'user/failtext/loginemailfail2.html'
        }
        return render(request, 'user/return/rpassword.html', context);

def changepasswordimpl(request):

    email = request.session['sessionemail'];
    pwd = request.POST['inputPassword'];
    pwd_confirm = request.POST['inputPasswordConfirm'];
    print('정보 입력 됨')

    request.session['sessionemail'] = email
    request.session['sessionpwd'] = pwd
    request.session['sessionpwd_confirm'] = pwd_confirm

    if pwd == '':
        print('비밀번호 입력하세요')
        context = {
            'center': 'user/failtext/updatefail.html'
        }
        return render(request, 'user/return/rchangepassword.html', context);

    if pwd_confirm == '':
        print('비밀번호 입력하세요')
        context = {
            'center': 'user/failtext/updatefail.html'
        }
        return render(request, 'user/return/rchangepassword.html', context);

    if pwd != pwd_confirm:
        print('비밀번호 불일치')
        context = {
            'center': 'user/failtext/updatefail2.html'
        }
        return render(request, 'user/return/rchangepassword.html', context);

    else:
        loginuser = userdao.select(email);
        UserVO.print(loginuser)
        userlist = []
        userlist.append(UserVO.print(loginuser));
        print(userlist[0][2])
        name = userlist[0][2]

        user = UserVO(email, pwd, name);
        userdao.update(user);
        context = {
            'rname': name
        };
        print('비밀 번호 완료')
        request.session['sessionid'] = name + '님'
        del request.session['sessionid'];
        return render(request, 'user/changepasswordok.html', context);