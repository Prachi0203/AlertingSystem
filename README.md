# Clean Bell
##### Avoid Contact Stay Intact

# Technologies used
- [Python](https://www.python.org/) 
- [OpenCV](https://opencv.org/)
- [Sinch](https://www.sinch.com/)

## Problem we are solving: 
Our vision is to avoid using doorbells to avoid Corona, instead when a person comes to someone's house he/she will look at camera then the camera sends notification to the user.
## Solution we have made:
It detects the face using webcam after detecting the face it sends notifications to the user. If face is not recognised it does not sends notifications to the owner.

### Use of Sinch
We have used Sinch to send messages to the user whenever the camera will detect any face.
The user will have to make an account on sinch then he/she can get the 'service_plan_id' and 'token' from them. After which the user can input the later in the code. The sender and recipients number also needs to be changed accordingly.
Sample :
![img](https://user-images.githubusercontent.com/59971890/103369725-e20c5e80-4af0-11eb-80bb-6f19ef60a5ef.png)

### How to run the program
Go to cmd and the directory in which the Cleanbell.py is then run the following command: 
```
python3 Cleanbell.py
```

### Youtube link for the implementation
- https://youtu.be/lK9VEIzOGI8


### Contributors of Project:
<table>
  <tr>
    <td align="center"><a href="https://github.com/kritikaparmar-programmer"><img src="https://avatars1.githubusercontent.com/u/59971890?s=460&u=f58bbd406bcbc2702101d9a2adf59e72e0cb838c&v=4" width="100px;" alt=""/><br /><sub><b>Kritika Parmar</b></sub></a></td>
    <td align="center"><a href="https://github.com/Prachi0203"><img src="https://avatars2.githubusercontent.com/u/58703496?s=460&u=bff1922e0bcb6878f039b9961a568cbad6021cbb&v=4" width="100px;" alt=""/><br /><sub><b>Prachi Bindal</b></sub></a></td>
    <td align="center"><a href="https://github.com/AayushSaini101"><img src="https://avatars1.githubusercontent.com/u/60972989?s=460&u=1f5c557fd1ce49c53307a129ae1ee42ccd1bb570&v=4" width="100px;" alt=""/><br /><sub><b>Aayush Saini</b></sub></a></td>
    <td align="center"><a href="https://github.com/abhi-146"><img src="https://avatars2.githubusercontent.com/u/58175317?s=460&u=cdd536b16ce399e0d400678a56808feb44c63448&v=4" width="100px;" alt=""/><br /><sub><b>Abhinav Jain</b></sub></a></td>
  </tr>
</table>