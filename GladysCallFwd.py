import rpa as r

#un = input ("What is your LDAP Username? ")
#pw = input("What is your ldap password? ")

un = 'Automation'
pw = 'vgYf9UeX7n23'

r.init(visual_automation=True)
r.url('https://172.16.1.15/ccmadmin/directoryNumberFindList.do')

#Only for First time Login
#r.click('Advanced')
#r.click('Proceed to 172.16.1.15 (unsafe)')

#Login into CUCM with stored LDAP Username/PW
r.type('//*[@name="j_username"]', un) 
r.type('//*[@name="j_password"]',pw)
r.click('cuesLoginButton') 
r.wait(5)


#Operator Extension 8006000 - adding callfwd to send calls to 8003535 - inside sales
r.keyboard('[tab]')
r.click('searchString0')

r.keyboard('8006000[enter]')
r.click('8006000') 
r.wait(5)

r.click('cfadestination')
r.keyboard('8003535')
r.click('Save')
r.wait('5')


#Operator Extension 8004000 - adding callfwd to send calls to 8003535 - inside sales
r.url('https://172.16.1.15/ccmadmin/directoryNumberFindList.do')
r.wait('5')

r.keyboard('[tab]')
r.dclick('searchString0')

r.keyboard('8004000[enter]')
r.click('8004000') 
r.wait(5)

r.click('cfadestination')
r.keyboard('8003535')
r.click('Save')
r.wait('5')


r.close()

