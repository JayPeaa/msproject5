  [![Build Status](https://travis-ci.org/JayPeaa/msproject5.svg?branch=master)](https://travis-ci.org/JayPeaa/msproject5)
# Milestone Project 5

  

  

  

#### Full Stack Frameworks

  

  

  

  

#### Design and Build an E-Commerce Site

  

  

  

  

  

### Website Name: Oakfield Farm Shop

  

  

  

  

##### See here for [Deployed App](https://msproject5.herokuapp.com/)

  

  

  

  

Oakfield Farm Shop is a concept for an e commerce site which allows users to purchase products online as well as advertising a family attraction. It enables users to browse various categories in the shop as well as research the farm as a place to visit. Users can contact the farm via a contact form and see the location via the google maps API. In addition the site has all the functionality you would expect with an e commerce site such as the ability to add products to a cart and proceed to purchase via the checkout which uses the Strip API. This app is built using Django which utilises an Object Relation Mapper (ORM) to seamlessly integrate an SQL relational database. The site also incorporates a number of other technologies.

  

  

  

  

Having an eye catching easy to use website acts as a calling card for any business so effort has been concentrated to create a pleasant user experience and user interface which allows users to quickly familiarise themselves with everything Oakfield Farm has to offer as well as an easy to navigate store.

  

  

  

  

## UX

  

  

  

  

The UX has been designed with the end user in mind and expectations in terms of front-end design are ever increasing, I opted to utilise Bootstrap4 for my design and responsive layout. Bootstrap is a library of UI components which aims to provide a unified and consistent user experience as well as responsive design.

  

  

  

Wire-framing was conducted using [Balsamiq](https://balsamiq.com/) and these are available to [view here](https://github.com/JayPeaa/msproject5/blob/master/Oakfield%20Farm%20Project.pdf)

  

  

  

#### User Stories

  

  

  

  

- As the app developer I want the website to clearly communicate what the business is about.

  

  

- As the app developer I want to create a visually appealing app with a quality feel. The feeling of quality and thoughtful design mirrors the products and brand values of the business.

  

  

- As the app developer I want products in the store to be presented in a user friendly way.

  

  

- As the app developer I want to include tools for user friendly and efficient browsing such as a searches and category filters. Filters should be clearly highlighted when active.

  

  

- As the app developer I want to create an app which is aesthetically pleasing with simple yet effective animation and well considered use of imagery.

  

  

- As the app developer I want a clear navigation menu with the most used aspects give their own space on an additional menu bar (Contact Page, Account Page and Basket)

  

  

- As the app developer I want the business owners to have a variety of marketing channels such as social media links and the ability to build mailing lists (subscribers).

  

  

- As an app developer I want the business to be able to advertise the bestselling products automatically

  

  

  

- As a user I want an easy to use online app.

  

  

- As a user I want to see important information display in prominent locations.

  

  

- As a user I want to be able to find products fast.

  

  

- As a user I want to be able to purchase any products with ease and purchase any products by bank card.

  

  

- As a user when viewing products in the store I want to be able to see key info at a glance (Servings, Weight, Price etc).

  

  

- As a user I want any payments I make to be safe and secure with reputable software.

  

  

- As a user I want to be able to update my profile information with ease.

  

  

- As a user I want to be able to have goods delivered to alternative addresses not just my invoice or home address.

  

  

- As a user I want to be able to subscribe to the latest offers or events.

  

  

- As a user I want to be easily able to locate the business

  

  

  

---

  

  

  

The design was focused around organic farming and nature, so earthy colours were used when considering the palette in order to compliment the design and theme. The site serves a dual purpose in that it advertises Oakfield Farm as a family attraction as well as an online shop.

  

  

  

Every effort has been made to make the advertorial aspect of the site as engaging as possible with use of well considered images and simple yet effective animations and hover effects. The e-commerce aspect has a user friendly store which includes filters and a search. As items are added to the basket the item count is displayed next to the basket menu option in the upper right of the screen. This provides visual feedback when items are added to the cart.

  

  

  

In order to provide a secure and safe environment for users all profile information is stored in a secure database. The site offers full profile functionality as well as the ability to reset forgotten passwords via an email link.

  

  

  

To enhance the user experience a more modern one-page theme has been designed for the products page. As new products are added cards are created in the online store and stacked using Bootstrap4 responsive grid/flex systems. The app makes use of flash messaging to confirm to the user when certain actions have been completed e.g. successful registration, payment or message submission. Pagination has not been used for this project as it was felt that on this occasion scrolling resulted in a better using experience. Scrolling is faster and is increasingly becoming second nature as a result of mobile devices.

  

  

  

---

  

  

  

A user may wish to perform the following actions:

  

  

  

- Register an account

  

  

- Log in or log out of their account

  

  

- Reset their password

  

  

- Update their profile information

  

  

- Have goods delivered to an alternate address than the one saved in their profile

  

  

- Browse and Filter products in the store

  

  

- Add items to their cart

  

  

- Pay for items on line in a secure environment

  

  

- Be able to easily contact the business by a variety of channels (Phone/Email/Post/Social Media/Contact Form)

  

  

- Subscribe to a newsletter

  

  

- Have clear instruction on how to locate the business

  

  

  

The site provides all these options to the end user and is very easy to use and navigate.

  

  

  

  

See here for [Wireframes](https://github.com/JayPeaa/msproject5/blob/master/wireframes_and_db_schema/Oakfield%20Farm%20Project.pdf)

  

  

  

  

## Database Considerations

  

  

  

  

Due to the relative complexity of this app an SQL database was selected. During the development phase SQLite was utilised as it comes inbuilt with the Django framework. As the project was nearing completion this DB was migrated to PostgreSQL. This was done with relative ease due to Django's Object Relational Mapper (ORM). Developing the models was the starting point for this data centric full stack project. See here for the [database schema](https://github.com/JayPeaa/msproject5/blob/master/wireframes_and_db_schema/Milestone%205%20Database%20Schema.pdf)

  

  

  

  

## Features

  

  

  

  

The main features of the App are:

  

  

  

  

- Clear and easy to use navigation

  

  

- Good use of colour and modern design

  

  

- Simple and effective animation techniques

  

  

- Fully responsive with a mobile first approach

  

  

- An online e-commerce store with integrated Stripe API for payments

  

  

- Relational PostgreSQL database with Create, Read, Update and Delete functionality

  

  

- A contact page with integrated Google Maps API

  

  

- Social media and email subscribe section for marketing

  

  

  

  

## Future developments

  

  

  

  

In the future it would be good to add some additional logic to this site to analyse trends and better forecast user demand. This will help the business owners with managing their stock levels. Making better use of the order history will obviously provide a myriad of other benefits.

  

  

  

Currently the site forces users to log in to the site at point of purchase so the introduction of a guest checkout is something that must be developed in the future to remove any unnecessary friction from the sales process resulting in loss of revenue.

  

  

The ability to create a user list of liked or regularly purchased products as well as the ability to filter by popularity would be a welcomed enhancement.

  

  

  

Security would need to be enhanced prior to making an app like this live.

  

  

  

The addition of instant messaging would provide another channel for customer to communicate with the business in real time.

  

  

  

Whilst there is a CMS available via Django it would be beneficial to create an intermediary CMS for superusers of the business as this will limit the potential for serious mistakes to made from having direct access to the inner workings of django.

  

  

The newsletter section currently contains logic which checks if a user is already subscribed and stores new email address in the database. It is not currently hooked up to any mail service. As a future development this will be connected to the mail chimp API in order to automate any social media campaigns.

  

  

Data Protections (GDPR) would also need to be given full consideration along with other legalities such as privacy policies, cookie notices and terms of service prior to making such an app available to use.

The site scored reasonably well during audit although some additional tweaks could be made relatively easily to bring the overall site performance up to 100%.

![Audit Result](https://github.com/JayPeaa/msproject5/blob/master/wireframes_and_db_schema/projectaudit.jpg)


  

  

  

  

## Technologies

  

  

  

  

The site is built using:

  

  

  

  

-  [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

  

  

  

-  [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

  

  

  

-  [Node Sass](https://github.com/sass/node-sass)

  

  

  

-  [javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

  

  

  

-  [jQuery](https://jquery.com/)

  

  

  

-  [Bootstrap4](https://getbootstrap.com/)

  

  

  

-  [Django](https://www.djangoproject.com/)

  

  

  

-  [Python](https://www.python.org/)

  

  

  

-  [PostgreSql](https://www.postgresql.org/)

  

  

  

  

#### CDNs and Library Usage

  

  

  

  

The following CDNs have been used to create this app.

  

  

  

  

##### Bootstrap &amp; Font Awesome

  

  

  

  

-  [https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)

  

  

  

-  [https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css](https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css)

  

  

  

  

##### jQuery &amp; Bootstrap

  

  

  

  

-  [https://code.jquery.com/jquery-3.3.1.slim.min.js](https://code.jquery.com/jquery-3.3.1.min.js)&quot;

  

  

  

-  [https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js)

  

  

  

-  [https://code.jquery.com/jquery-3.3.1.slim.min.js](https://code.jquery.com/jquery-3.3.1.slim.min.js)

  

  

  

  

## Testing

  
Travis has been implemented on this project for continuous integration and testing. Unit tests were set up for each of the apps in a test.py to test certain aspects of the Models, Forms, URLs and views. These tests ensured that Models correctly posted to the DB, required fields worked in the forms as expected and URLs resolved correctly among other things.

Travis Current Status:     [![Build Status](https://travis-ci.org/JayPeaa/msproject5.svg?branch=master)](https://travis-ci.org/JayPeaa/msproject5)
  

  

  

To ensure any database postings were as anticipated it is common practice to print to the console to determine if the outputs and data structures were as expected. This was done prior to allowing user input to be posted directly to the database collections.

  



  



  

  

  

  

During user acceptance testing it became evident that additional controls were required on form inputs to maintain the visual appeal of the app as well as prevent unusual input. Maxlength, Min, Max and required attributes and classes were used to make the app more robust.

  

  

  

  

Testing has been conducted using Firefox developer dev tools. Thorough testing in all the various mobile devices along with general responsiveness (responsive mode) has concluded that this site works well in all modern-day browsers and mobile devices. As part of the testing process each page has been reviewed systematically to ensure all links work as intended and the pages display correctly.

  

  

  

  

This testing has confirmed that users will be able to utilise the website as intended on any device (in landscape or portrait mode) to achieve their goals whilst enjoying the experience and customer journey.

  

  

  

  

All user forms display correctly and as intended on various displays / devices.

  

  

  

  

All CSS, HTML and JavaScript was run through code validators and flint to ensure any error were remedied. [Flake8](http://flake8.pycqa.org/en/latest/) was used to ensure that any python code was PEP8 compliant.

  

  

  

  

### Browser Compatibility Testing

  

  

  

  

#### Issues Encountered

  

  

  

  

Time was invested at the start of the project to ensure HTML code and Bootstrap Classes were working as anticipated, which saved some time on responsiveness testing during the latter stages of the build. Although during testing it became apparent that the wrong class had been used for extra small screens e.g. col-xs-12 instead of col-12. Some additional work was needed for medium screens so grid sizes were adjusted for the MD classes.

  

  

The project was tested in various browsers including Firefox, Chrome, Opera and Edge.

  

  

  

HTML and CSS Validators were used to clear any errors, however, HTML validation tends to highlight any Django templating as errors when they are not e.g. {{ order_form }} or {{ total }}. The HTML code validators also highlighted some certain issues with regards to missing closing tags and inappropriate tag nesting which have now been resolved.

  

  

Flake8 was used to ensure that any python code was in line with PEP8 standards and a number of minor issues were detected and resolved. Flake8 also detected various imports that were implemented but no longer being used as processes changed during the development stage. These have now been removed.

  

  

Some minor modifications were made to the layout of my design, post wireframing, which were straightforward to implement. This was done in order to achieve more balance visually.

  

Hard coded routes were replaced with `{ tags }`during the development phase to prevent potential hacking of the database.

  

  

Testing the deployed app highlighted some additional errors, which were database related, as the application was unexpectedly running in development mode. This meant the migrations to the PostgreSQL database had failed. This was identified by setting the 'Development' config var in Heroku to True and recreating the error and examining the error message. This provided more detail as to the cause of the error than the Heroku logs. In order to ascertain which DB Heroku was using the python shell was used to import the settings and then settings were printed to the console. This demonstrated that Heroku was still referencing the SQLite database used during development. This issue was created as a result of the development variable being incorrectly located in the .env file. Once this was removed and set within Git-pod development was set to false and the PostgreSQL database was referenced. Whilst in the Heroku CLI tool the `makemigrations` and `migrate` commands were run again in order to ensure that the PostgreSQL was up to date.

  

  

  

## Deployment

  

  

  

Throughout the projects regular git commits were made to ensure any working files were backed up. Numerous commits have been logged on the main branch in GitHub. No additional branches were created when working on this project as there were no other collaborators. Although it may have helped from an organisation point of view had I created additional branches for specific sections of the project. Using git checkout to switch between branches in the terminal along with push, pull and merge requests to incorporate all change on the main branch following review would have represented best practice had there been multiple collaborators. The project has been successfully deployed on [Heroku](https://www.heroku.com/).

  

  

  

  

[Gitpod](https://www.gitpod.io/) has been used throughout this project as the IDE of choice.

  

  

  

Issues were encountered when initially deploying the app to Heroku. This was due to Heroku auto detecting Node's package.json file and creating a Node build pack rather than a Python build pack. In order to rectify this issue, the build pack was manually deleted in Heroku and replaced with a python build pack. The package.json file was then removed before pushing the app to Heroku. After the app was successfully deployed to Heroku the package.json file was reinstated.

  

  

In preparation for final deployment to Heroku the following procedure was followed:

  

  

- First conceal any secret keys by setting environment variable in the `.env` file. [Dotenv](https://pypi.org/project/python-dotenv/) was used for this and can be viewed in settings.py

  

  

  

- The secret keys were then added to the config vars within Heroku.

  

  

- Ensure the DEVELOPMENT variable is set to False in settings.py

  

  

- Confirm the Procfile and requirements.txt files have been updated.

  

  

- Once the above has been completed use the following commands to push to github.

  

  

```

  

  

python3 manage.py collectstatic

  

  

```

  

  

When prompted to confirm type `YES`

  

  

```

  

  

git add .

  

  

  

git commit -m "Final Commit"

  

  

  

git push origin master

  

  

  

```

  

  

  

- Heroku is linked to the Git Repository and set to Auto Deploy so there is no requirement to push any code to Heroku separately.

  

  

  

---

  

  

  

  

### File Structure

  

  

  

  

The project has been organised as follows:

  

  

  

  

```

  

  

  

ROOT DIRECTORY

  

  

  

  

msproject5 (Project folder)

  

  

  

node_modules (folder)

  

  

  

cart (App folder)

  

  

  

orders (App folder)

  

  

  

pages (App folder)

  

  

  

products (App folder)

  
  

readme_and_db_schema (folder)

  

  

search (App folder)

  

  

  

static (folder)

  

  

  

staticfiles (folder)

  

  

  

templates (file)

  

  

  

users (App folder)

  

  

  

.env

  

  

  

.gitignore

  

  

  

manage.py

  

  

  

license.md

  

  

  

  

Package-lock.json

  

  
  

  

  

requirements.txt

  

  

  

```

  

  

App folders typically follow the same structure. A typical example is shown below:

  

  

  

```

  

  

users (App folder)

  

  

__pycache__ (folder)

  

  

migrations (folder)

  

  

templates (foldeer)

  

  

__init__.py

  

  

admin.py

  

  

apps.py

  

  

forms.py

  

  

models.py

  

  

tests.py

  

  

views.py

  

  

urls.py

  

  

```

  

  

  

  

##### Gitignore

  

  

  

The node_modules file includes a number of dependencies which are required to run node sass. This was included in the gitignore file along with package-lock.json. In addition a standardised template was used to include other common file types for a python project of this type [gitignore.io](https://www.gitignore.io/api/python)

  

  

  

  

  

The [SCSS](https://sass-lang.com/documentation/syntax) folder includes my main.scss file which compiles my CSS. A script is included within my package.json file to run this using the `run sass` command.

  

  

  

  

`"sass": "node-sass -w scss/ -o static/css/ --recursive"`

  

  

  

  

The static folder structure is as follows:

  

  

  

  

```

  

  

  

static (folder)

  

  

  

admin (folder)

  

  

  

CSS (folder)

  

  

  

main.css (file)

  

  

  

images (folder)

  

  

  

(various image files)

  

  

  

js (folder)

  

  

  

checkout.js(file)

  

  

  

```

  

  

  

  

Where django apps have dedicated HTML templates, these pages are located within the templates folder of the app. Generic HTML pages or page sections are located in the templates folder in the root:

  

  

  

  

```

  

  

  

templates (folder)

  

  

  

advertorial.html (file)

  

  

  

base.html (file)

  

  

  

contact.html (file)

  

  

  

hero.html (file)

  

  

  

home.html (file)

  

  

  

password_reset_confirm.html (file)

  

  

  

subscribe.html (file)

  

  

  

```

  

  

  

  

  

## Author

  

  

  

- John Hay - Code Institute Student

  

  

  

  

  

## License

  

  

  

  

Released under the MIT [license](https://github.com/JayPeaa/milestone4-cook-e/blob/master/license.md)

  

  

  

  

  

## Credits

  

The following code snippet was provided by slack user czk8780 to solve an issue regarding formatting telephone numbers on forms.

  

```

def __init__(self, *args, **kwargs):

super().__init__(*args, **kwargs)

self.fields['order_phone_number'].widget.attrs['pattern'] = "[0-9]{1,15}"

```

  

  

  

### Images and Media

  

  

  

  

All images and media used on this site have been labelled for reuse / non-commercial and are for educational purposes only. Sites included [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/)

  

  

  

  

### Acknowledgments

  

  

  

  

Special thanks to the Code Institute Slack Community CI Tutors and project mentor Tony Montaro for support and guidance provided during this project.

  

  

  

  

---
