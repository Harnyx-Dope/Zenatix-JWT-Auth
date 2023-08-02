# Zenatix-JWT-Auth
<h1>This is the Event Management System containing JWT- Authentication Based Rest-API's!!!</h1>
<h1>#MITM(Man-in-the-middle) Attack Using Proxy Server(Burp-Suite)</h1>
<h1>JWT Auth Vulnerability check is done by Burp-Suite </h1>
Here are Some  ScreenShots checking and intercepting token:-
<h3>Have Setted the Burp-Suite</h3> and open the browser for the same

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/f246babc-6c45-45ef-86c7-09c4119d330b)
<h3>Event- Management System is Basically used to access the Events of a registered admin in db(superuser)</h3>

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/dc48eae1-7dd4-4f8e-910c-59f3dcbe9c69)
<h3>Creating Super User in DB</h3>

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/67be4157-2edf-43a6-8760-abc09c35ca9a)
<h3>Basically  for Burp Intercepting ,i will ask for token with registered user</h3>
Steps are as follows:-

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/2435f693-7ae3-4c1f-96b1-f271abcd1e80)

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/186a10c5-e519-4ba4-a0f9-0122a597cce8)
We have token now 

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/cc97062d-9f9e-4cf5-9d61-af4056fe3eb3)
But the interceptor Can also Render that token
![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/9c587de8-95f6-4abf-a04e-f8053662b812)
<h3>Now we will navigate to Event List</h3>

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/57f2dd9f-0b71-4a6b-a2c7-0bdb7b68a09e)
<h3>It will ask the Interceptor for auth details</h3>

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/7cb2d49b-03cf-4cc7-8705-87bef4fa61dd)
<h2>He Can Change the Payload request from Burp-Suite As Well!!! acting as MITM</h2>

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/7e0788c9-5055-4537-8622-e14b21838416)
<h2>Then, It is accessible and JWT-Auth is Vulnerable</h2>

![image](https://github.com/Harnyx-Dope/Zenatix-JWT-Auth/assets/85693353/0e1072bf-8f0e-4fb8-9fa8-ef4fc28d5611)

