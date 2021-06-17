import random
when = ['A few years ago','Yesterday','Last night','A long time ago','On 19th Nov']
who=['a rabbit','a parrot','an elephant','a turtle','a cat']
name=['Bhuvitha','Ravi','Teja','Ashwin','Rishi']
residence=['Belgium','Texas','New York','India','London']
went=['cinema','university','seminar','school','laundry']
action=['made a lot of friends','ate a burger','found a secret key','solved a mistery','wrote a book']
print(random.choice(when)+' , '+random.choice(who)+" whose name is "+random.choice(name)+' ,'+' that lived in '+random.choice(residence)+', went to the '+random.choice(went)+' and '+random.choice(action))
