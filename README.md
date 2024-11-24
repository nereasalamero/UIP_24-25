# UIP_24-25
Exercises developed in User Interface Programming, a subject I did while I was studying as an exchange student at Savonia UAS.

### Exercise 2
#### PART I:
Try out the Hello World app and change it to "Hello IoT", color to "blue", and size to 35.
#### PART II
- Read the counter app code
- Change the increment/decrement to 2^n (where n is every increase or decrease in integer values)
- Start from n=0

### Exercise 3
Create an UI that can input name and the university and print them in as a list when a button is clicked. Add another button that can display a dialog.

### Exercise 4
Create a multi-counter Flet app where user can create and delete counters with names.

### Exercise 5
Create a Flet picture viewer app with a login page, form page and show details page.
- Use an app bar to go back.
- Show error message when email or password is not entered.
- Add button on the home page to navigate to the form.
- The form page consist of textfields where you can enter the name, date of birth, sex, address, and country. Use datepicker, drowpdown, radio buttons.

Use flet card to show the details https://flet.dev/docs/controls/card/

### Exercise 6
Try out the timer app in https://flet.dev/docs/getting-started/async-apps

To run something in the background use page.run_task()

- Create a flet multi countdown timer app with the following features:
  - Create three timer tabs (see https://flet.dev/docs/controls/tabs/).
  - Each tab contains: a) start value of timer, b) start, pause and reset buttons, c) the remaining time, and d) a progress bar/progress ring.
  - User can start and stop timers asynchronously and switch between them with the tabs.
  - Try to use navigation drawer instead of tabs.

### Exercise 7
Create an encrypted chat app in Flet where users can set their passphrase and send and receive messages.
- Users will enter the passphrase as text.
- Users can select a specific topic to subscribe/send to using a drop-down menu.
- Users with the correct passphrase should be able to decrypt the messages sent.
- Refer encrypt and pubsub pages for details.
- Refer to the example chat app here for inspiration.

### Exercise 8
Create a Flet app to add daily expenses in 4 different categories and display each entries in a table. Update a pie chart that displays the share of expenses in the different categories.

(Hint: append a DataRow with DataCell in the row of the DataTable)

- Refer to PieChart control.
- Refer to DataTable control.
- Create a short form with autocomplete, textfield, and submit button.
