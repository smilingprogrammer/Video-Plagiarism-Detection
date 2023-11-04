<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Video Plagiarism Detection</h3>

  <p align="center">
    A python package that ease the detection of plagiarized videos using AI
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Implementation-and-Usage">Implementation and Usage</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About This Project

This project is built for the detection of plagiarized videos mostly on online platform. It is built as a python package to ontegrate detection of videos with same similarities for most online video platforms. If integrated into an online video platforms codebase and barcode images of the codebase are generated, It calculate the similarities between newly uploaded video and another videos. This ease the use for the manual banning of videos due to plagiarism.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The following contains list of major frameworks/libraries i used to bootstrap this project. Here are some

* [![Python][python]][python-url]
* [![Pytorch][pytorch]][pytorch-url]
* [![Numpy][numpy]][numpy-url]
* [![Open-CV][open]][open-url]
* [![PyPi][pypi]][pypi-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The code can be setup either locally or on any virtual machine.

### Prerequisites

- Any command line
- Or an IDe

### Implementation And Usage

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Make sure you have the python installed on your machine.
2. Converts the videos into barcodes.
3. pip install the package in your cli
   ```sh
   !pip install Vidbarcodesimilarities
   ```
4. Then use the vidbarcodesimilarities function to run the video similarities.
   ```sh
   Vidbarcodesimilarities.vidbarcodesimilarities("/path", "/path")
   ```
5. Make sure the "/path" contains path to the barcodes

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add automatic conversions of videos to barcodes
- [x] Increase the model performance.
- [ ] Train the model on higher GPU to increase performance.
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi media support
    - [ ] Text
    - [ ] Audio

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

Abdulsobur Oyewale - [@sprogrammerx](https://twitter.com/sprogrammerx) - Abdulsoburoyewale@gmail.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[pytorch]: https://img.shields.io/badge/Pytorch-20232A?style=for-the-badge&logo=pytorch&logoColor=61DAFB
[pytorch-url]: https://pytorch.org/
[numpy]: https://img.shields.io/badge/Numpy-35495E?style=for-the-badge&logo=numpy&logoColor=4FC08D
[numpy-url]: https://numpy.org/
[open]: https://img.shields.io/badge/OpenCv-DD0031?style=for-the-badge&logo=opencv&logoColor=white
[open-url]: https://opencv.org/
[pypi]: https://img.shields.io/badge/PyPi-4A4A55?style=for-the-badge&logo=pypi&logoColor=FF3E00
[pypi-url]: https://pypi.org/
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
