<div align='center'>
  

  <h1>Pan Card Tampering Detection Streamlit App</h1>

  <p>
  This is a Streamlit app that allows users to upload an image of a PAN card and detect if there has been any tampering. The app also calculates the structural similarity index (SSIM) between the uploaded image and a reference image to validate the ID.
  </p>

<!-- Badges -->

<a href="https://priyanshu88-diabestes-prediction-streamlit-app-main-5komds.streamlit.app/" target="_blank">![](https://img.shields.io/website-up-down-green-red/http/monip.org.svg)</a>
![](https://img.shields.io/badge/Maintained-Yes-indigo)
![](https://img.shields.io/github/forks/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App.svg)
![](https://img.shields.io/github/stars/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App.svg)
![](https://img.shields.io/github/issues/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App)
![](https://img.shields.io/github/last-commit/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App)
  
 
 <h4>
    <a href="https://priyanshu88-diabestes-prediction-streamlit-app-main-5komds.streamlit.app/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App/blob/master/README.md">Documentation</a>
  <span> · </span>
    <a href="https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App/issues">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App/issues">Request Feature</a>
  </h4>
</div>

<br />


<!-- Table of Contents -->

## :notebook_with_decorative_cover: Table of Contents

- [Image](#signal_strength-image)
- [Dependencies](#toolbox-dependecies)
- [Installation](#gear-installation)
- [Usage](#play_or_pause_button-usage)
- [Deployment and Notebook](#triangular_flag_on_post-deployment-and-notebook)
- [License](#balance_scale-license)
- [Contact](#handshake-contact)



## :signal_strength: Dataset

This project has a wide dataset scope but for the reference of example we have worked on Permanant Account Number issued for indians to verify their identity. The reference image looks like below:

<div align='center'>
<img  src='https://user-images.githubusercontent.com/86107841/236691772-cefaee43-31fc-4f72-85b9-7d9611be3971.png'/>
</div>


## :toolbox: Dependecies


`streamlit`

`numpy` 

`scikit-image==0.18.3`

`imutils==0.5.4`

`opencv-python-headless`

`Pillow==8.3.1`



## :gear: Installation

Clone the repository and install the required dependencies using the following commands:

```bash
git clone https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App.git
```

```bash
cd Pan-Card-Tampering-Detection-Streamlit-App
```

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```

## :play_or_pause_button: Usage

1. Open the app in your web browser through the provided link.
2. Click on the "Choose an image file" button to upload an image of a PAN card.
3. The app will process the image and display the original and processed image side by side.
4. If any tampering is detected, the app will highlight the tampered area in red.
5. The app will display a message indicating whether tampering was detected or not.
6. The app will also display the structural similarity index (SSIM) between the uploaded image and the reference image.




## :triangular_flag_on_post: Deployment and Notebook

This tool has been deployed using [`Streamlit`](https://streamlit.io/). Learn about streamlit deployment [`here`](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app). Checkout the notebook repository [`here`](https://github.com/Priyanshu88/Pan-Card-Tampering-Detection).



## :balance_scale: License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App/blob/main/LICENSE) file for details.



## :handshake: Contact

![](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)

Your Name - [@twitter_handle](https://twitter.com/Priyans75729802?s=09) - 2040020@sliet.ac.in

Project Link: [https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App.git](https://github.com/Priyanshu88/Pan-Card-Tampering-Detection-Streamlit-App.git)
<hr />
<br />
<div align="center">Don't forget to leave a star ⭐️</div>
