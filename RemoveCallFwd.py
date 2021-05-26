import rpa as r
from tagui import exist

#un = input ("What is your LDAP Username? ")
#pw = input("What is your ldap password? ")

un = 'Automation'
pw = 'vgYf9UeX7n23'

r.init()
r.url('https://172.16.1.15/ccmadmin/directoryNumberFindList.do')

#Only for First time Login
if r.exist('Advanced'):
    r.click('Advanced')


if r.exist('Proceed to 172.16.1.15 (unsafe)'):
    r.click('Proceed to 172.16.1.15 (unsafe)')

#Login into CUCM with stored LDAP Username/PW
if r.exist('j_username'):
    r.type('j_username', un) 


if r.exist('j_password'):
    r.type('j_password',pw)


if r.exist('cuesLoginButton'):
    r.click('cuesLoginButton') 


r.wait(10)

r.url('https://172.16.1.15/ccmadmin/directoryNumberFindList.do')

#Operator Extension 8006000 - adding callfwd to send calls to 8003535 - inside sales
r.type('searchString0', '[clear]')
r.type('searchString0', '8006000')
r.click('findButton')
r.wait(10)
r.click('8006000') 
r.wait(10)

r.type('cfadestination', '[clear]')

r.click('Save')
r.wait(5)

#Operator Extension 8004000 - adding callfwd to send calls to 8003535 - inside sales

r.url('https://172.16.1.15/ccmadmin/directoryNumberFindList.do')
r.wait(10)

#Operator Extension 8004000 - adding callfwd to send calls to 8003535 - inside sales
r.type('searchString0', '[clear]')
r.type('searchString0', '8004000')
r.click('findButton')
r.wait(10)
r.click('8004000') 
r.wait(10)

r.type('cfadestination', '[clear]')

r.click('Save')
r.wait(10)

r.close()

