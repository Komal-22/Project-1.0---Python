#!/usr/bin/env python
# coding: utf-8

# In[1]:


firstName = str(input("Enter your first name: "))
lastName = str(input("Enter your last name: "))


# In[3]:


fullName = firstName + " " + lastName
print(fullName)


# In[4]:


standard = str(input("Enter your standard: "))
division = str(input("Enter your standards' division: "))


# In[7]:


rollNo = int(input("Enter your Roll No.: "))


# In[8]:


firstSubject = str(input("Enter the name of first subject: "))
secondSubject = str(input("Enter the name of second subject: "))
thirdSubject = str(input("Enter the name of third subject: "))


# In[9]:


marksInFirstSubject = float(input("Enter marks obtained in " + firstSubject + ": "))
marksInSecondSubject = float(input("Enter marks obtained in " + secondSubject + ": "))
marksInThirdSubject = float(input("Enter marks obtained in " + thirdSubject + ": "))


# In[10]:


totalMarks = marksInFirstSubject + marksInSecondSubject + marksInThirdSubject
print(totalMarks)


# In[11]:


percentage = totalMarks/3
print(percentage)


# # Student Portfolio

# In[14]:


print("Name: " + fullName)
print("Class: " + standard + " " + division)
print("Roll No: " + str(rollNo))
print("Name of all three subjects: " + firstSubject + ", " + secondSubject + ", " + thirdSubject)
print("Total Marks obtained in above mentioned in three subjects is: " + str(totalMarks))
print("Percentage obtained by " + fullName + " is " + str(percentage))


# In[ ]:




