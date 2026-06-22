# Project Requirements

## Identified Problem or Need

Meals are often planned last minute which means that they are often made from whatever
the household has on hand. People often want to make meal plans to be more productive
but there is a lot of friction in doing so.

Households with meal planning already in place often use paper systems which are unreliable as
they are easy to lose or damage and can only be accessed from the piece of paper itself

## End-User Requirements

The end-users for this project are full households so requirements will vary greatly between
groups and individuals so its important to make the system very easy to use at base level
but allow more advanced users the option to take shortcuts

## Proposed Solution

My solution for the above problem I plan to create an app that allows a user to create a household
and other members of the household will join this family and are then able to plan out meals by
copying in links for recipes.

# Relevant Implications

## Functionality

An application meeting functionality expectations means that it works well on all devices,
there are no bugs or glitches and that all links and elements work as expected

### Relevance to the System

For this application to be successful in solving the problem it needs to work properly and effectively.
If the app has a lot of bugs and broken links etc this gives friction to the user meaning that they
are less likely to enjoy the application and therefore won't use it again in the future.

### Impact / Considerations

I will need to ensure that any new features or edits to old ones are thoroughly tested to catch bugs
and remove them before production. I will also test to make sure load times remain around a second to 
keep user interest

 I plan to improve functionality by:

- Testing every button, form, and link before publishing updates
- Checking the site on mobile, tablet, and desktop devices

## Usability

An application meeting useability expectations means that it is easy and intuitive for the user to use
following Nielson's heuristics and common conventions are important for this

### Relevance to the System

For this application to be successful in solving the problem it needs to be easy and intuitive to use.
If the app is confusing or frustrating for the user this gives friction to the user meaning that they
are less likely to enjoy the application and therefore won't use it again in the future.

### Impact / Considerations

I will need to ensure that I routinely refer back to Nielson's heuristics and common convention to make
sure my app is as pain-free to use as possible. 
I will also make sure I am:
- Keeping navigation and buttons consistent across all pages
- Showing clear feedback messages (e.g. loading, success, error)

## Accessability

An application meeting accessability expectations means that is able to be used by anybody regardless of
any disability such as impaired vision, poor hearing, dyslexia, colour blindness and also that the app is
accessible on any device eg phone, tablet, computer

### Relevance to the System

For this application to be successful in solving the problem it needs to be accessible to any end-user
as anybody could be using it so making sure it caters to all people regardless of disability or device etc
because if not then that user will simply not be able to use the application and a user will be lost

### Impact / Considerations

I will need to ensure that use semantic HTML tags (header, main, nav, section, etc.) and alt text for images to allow people using screen readers
use the site. I will also need to ensure that there is good colour contrast between text and backgrounds
so that the text is easily readable which also adds to useability in the process

## Privacy

An application meeting privacy expectations means that it will only store necessary information for the app
to operate and will take measures to keep this data private. I will also ensure I adhere to privacy laws 
such as the Privacy Act 2020

### Relevance to the System

This application will use an account system which means I will need to collect data from users the piece
of data that is particularly prevalent here is the users password which will need to be stored securely 
within the database of the app

### Impact / Considerations

I will make sure that I only ever collect necessary data for the operation of the app. Passwords will not be
stored instead I will store hashes of the passwords so not even I/the app will know the password.
I will also add a clear privacy note explaining what data is collected and why

## End-user

A design that considers end-users should be built around the real people who will use it ensuring that the interface
caters to any specific need and completes the tasks that the end-user want to complete in an efficient manner

### Relevance to the System

My app will cater to a wide variety of people from a wide range of demographics so ensuring that it caters to as many 
of these people as possible is very important to make sure as many people can use the app effectively as possible

### Impact / Considerations

I plan to meet end-user requirements by:
- Writing content in a way that is accessible to all age groups and levels of education
- Prioritising the main tasks users want to complete quickly
- Making the interface as easy to use as possible for someone who is not very tech literate by using large obviously 
labelled buttons etc

## Intellectual property

Using peoples creative work without their permission and consent is illegal this includes images, fonts, music and code

### Relevance to the System

Within this system I want to use appealing images and fonts to make the website aesthetically pleasing which means I may use copyrighted material

### Impact / Considerations

I plan to manage intellectual property by:

- Using only original assets or media with a valid licence
- Keeping a source list with credits and licence details
- Checking that anything I use has the correct licence for me to use
- Using non-copyright resources wherever possible

# User Experience (UX) Principles

## Consistent and clear/ clear, and helpful language

I user will learn the interface faster when the design and interactions are consistent and clear language
helps greatly with this

### Relevance to the System

People using this app want it to be quick and convenient otherwise there will be too much friction and users will
give up and not plan meals if they are able to learn the system easily it will become quick and easy

### Impact / Considerations

To make sure that create a system that is consistent, clear and helpful, I will:

- Come up with a design system that takes into account the needs of the end-users
- Discuss layouts and prototypes with end-users to ensure they are clear
- Use CSS variables and Jinja templates to keep things the same across pages
- Use text that meets the needs of my end-users in terms of reading level
- Label buttons and other UI elements with clear labels that convey exactly what it 
will do in a concise way e.g. save changes instead of submit


## Test and improve

Testing a system ensures that the code you have written works as intended and allows you to make improvements
on the app afterward based on feedback

### Relevance to the System

This app is made with end-users in mind so making sure that the app works for them and not just me by testing is 
important. I also need to ensure I meet functionality standards and by testing and bug fixing I can ensure this.

### Impact / Considerations

To make sure that the system gives the best possible UX for my users, I will:

- Test features as I implement them to make sure any bug fixes later don't require fixing 
a long list of other cascade issues
- Regularly test the design and working system with end users to gather feedback
- Act upon the feedback to improve the system at every stage
- Use a code validator at the end of each sprint or milestone completion

## Know your user

Knowing your end user means considering the demographic you are making an app for and ensuring that it 
caters to any specific needs these groups have

### Relevance to the System

My app is made with end-users in mind which means I need to make sure I am meeting their requirements at all points
of the process

### Impact / Considerations

To make sure that I know my users well, and that the system works well for them, I will:

- Talk to my end-users to discover specific needs they have
- Regularly test my ideas, designs and the system with the end-users to see what is working well or not
- Make sure I am meeting accessability requirements to cater to users with specific accessability needs
- Make sure the app is responsive to different types of devices and screen sizes
