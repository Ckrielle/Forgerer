# Forgerer
> The (to-be) Definitive CSRF Website Creator

## Table Of Contents
* [General Info](#general-info)
* [Installation](#installation)
* [Demonstration](#demonstration)
* [To-Do](#to-do)
* [Donations](#donations)
* [Contact Me](#contact-me)
* [License](#license)

## General Info
**CSRF**: CSRF stands for Cross Site Request Forgery. Essentially wherever a request can be made in a website, you can write your own site that sends that request impersonating the user you sent your malicious 
link to (follow the link for a more thorough explanation). This attack can delete users account, delete their posts/post whatever to their account, generally do whatever the site allows without the users authentication. It is a common vulnerability with usually medium impact that can lead to other attacks, such as stored XSS. This tools aim is to automate the attack, not only to increase the productivity of bug hunters, but to make the investigation of this attack accesible to everyone.

**Explanation**: The tool takes the provided url and displays every action, method and parameters it can find. After that the user can specify which form he wants to create a website with, and one by one the different parameters are presented, offering the user the possibility to give his/her value of choice. After that is done the website is generated in index.html and the website is ready.

***Important: I am in no way responsible or accountable for any malicious usage of the tool. It was created for educational purposes and to help white hats. If you intend to use it for illegal activites then
just don't and take time to fully grasp the severity of your possible actions.***

## Installation

All you have to do is copy paste the commands below into your terminal.
```
git clone https://github.com/Ckrielle/Forgerer.git
cd Forgerer
sudo pip3 install -r requirements.txt
```
## Demonstration

> Under Construction

## To-Do

I could leave it as it is however there are imporvements I intend on implementing:
* Integrate argparse.
* Create different websited for different type of requests along with POST which is the default (GET, DELETE, ...).
* Prettify it (Colors, Banner, ...).
* Deploy it to the web.
* Options for possible csrf token (Deletion, Include one of same length, ...).
* Choosing to create one, some, or all possible CSRF sites.
* Obviously fix any bug that is found.
And whatever else comes to my mind at a later time.

## Donations

If for some reason you think I deserve money for having written this or any of my other projects, firstly thank you very much I'm humbled. Secondly you can buy me a penguin!

<a href="https://www.buymeacoffee.com/Machina" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-pink.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;" ></a>

## Contact Me

You can find me on [Twitter](https://twitter.com/3xM4ch1n4).

## License

See LICENSE for more info.
