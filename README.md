# Clean Bell
### Avoid Contact Stay Intact

# Technologies used
- [Python](https://www.python.org/) 
- [OpenCV](https://opencv.org/)
- [Sinch](https://www.sinch.com/)

## Problem we are solving: 
Our vision is to avoid using doorbells instead when a person comes to someone's house he/she will look at camera then the camera sends notification to the user.
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
    <td align="center"><a href="https://github.com/kritikaparmar-programmer"><img src="" width="100px;" alt=""/><br /><sub><b>Kritika Parmar</b></sub></a></td>
    <td align="center"><a href="https://github.com/Prachi0203"><img src="" width="100px;" alt=""/><br /><sub><b>Prachi Bindal</b></sub></a></td>
    <td align="center"><a href="https://github.com/"><img src="" width="100px;" alt=""/><br /><sub><b>Aayush</b></sub></a></td>
    <td align="center"><a href="https://github.com/"><img src="" width="100px;" alt=""/><br /><sub><b>Abhinav Jain</b></sub></a></td>
  </tr>
</table>