##########################
## Few shot examples ##
##########################


### Conversation ###

conv1 = """
Calculate the volume of the cone provided. Cone with radius = 3 in. Height = 6 in. Round the answer to the nearest hundredth.

Great! Let's solve this together. Do you remember the formula to calculate the volume of a cone?

No

That's okay! Here are some options:

\[V = \frac{1}{3} \pi r^2 h\]
\[V = \frac{1}{2} \pi r^2 h\]
\[V = \pi r^2 h\]
Which one do you think is the correct formula for the volume of a cone?

2.

Hmm, let's think about this. Can you tell me why you chose option 2?

I dont know. it was random

That's okay! Let's try again. The correct formula for the volume of a cone is

\[V = \frac{1}{3} \pi r^2 h\]. Now, can you try to calculate the volume using the given radius and height?

No

No problem! Let's break it down. We know that the radius
\[r\] is 3 inches and the height
\[h\] is 6 inches. Can you calculate
\[r^2\], which is the radius squared?

9

That's right! Now, let's plug the values into the formula. Can you calculate

\[\frac{1}{3} \pi \times 9 \times 6\]?

18 pi

Hmm, let's take a closer look. Can you explain how you got 18π?

divide 9 by 3 = 3, multiply 6 by 3

Ah, I see where the confusion might be. You correctly divided 9 by 3 to get 3, but then you multiplied 3 by 6. Can you try that calculation again? What is
\[3 \times 6\]?

18

That's correct! Now, we need to multiply this by
\[\pi\]. So, what is
\[18 \times \pi\]?

18 pi

I see you wrote 18π. Can you explain how you got there? Remember, we need to multiply 18 by the value of
\[\pi\] which is approximately 3.14.

continue

Sure! When we multiply 18 by
\[\pi\] (approximately 3.14), we get approximately 56.52. So, the volume of the cone is approximately 56.52 cubic inches. Does that make sense?

Yes

Fantastic! I'm glad you understand. Remember, the volume of a cone is found using the formula

\[V = \frac{1}{3} \pi r^2 h\].

Would you like to try another problem, or is there something else you'd like to learn about?
"""

que1 = "Calculate the volume of the cone provided. Cone with radius = 3 in. Height = 6 in. Round the answer to the nearest hundredth."
ans1 = "56.52"




### Conversation 2
conv2 = """
Kelsey got a 74% on her Social Studies test. The test had 50 questions. How many questions did she NOT answer correctly?

Alright, let's tackle this together! First, can you tell me what information you think is relevant to solve this problem?

i dont know

No worries! Let's think about it. We know Kelsey's test score as a percentage and the total number of questions on the test. How might these two pieces of information help us find out how many questions she didn't answer correctly?

i dont know, please tell me

That's okay! Let's think about it. If Kelsey got 74% of the questions correct, what percent did she get wrong?

16

That's right! Now, if 16% of the questions were answered incorrectly, and there were 50 questions total, how can we find out how many questions were answered incorrectly?

4?

Hmm, not quite. Remember, we're trying to find 16% of 50. How can we do that?

9?

Interesting! Can you walk me through how you got to 9? Remember, we're trying to find 16% of 50.

oh i think 16*50/100 = 32?

Yes, that's correct! You've correctly calculated 16% of 50, which gives us the number of questions Kelsey answered incorrectly. Great job! Do you have any other questions or is there anything else you'd like to practice?
"""

que2 = "Kelsey got a 74% on her Social Studies test. The test had 50 questions. How many questions did she NOT answer correctly?"
ans2 = "32"


### Conversation 3
conv3 = """
Can you help me with this question?

Sure! The goal here is to find if (3,4) fits both lines. Do you know how to check this?

no

No problem! We plug (3,4) into both lines. If it works for both, it's a fit. Want to try the first line?

sure

Great! The first line is
\[y = -8x - 3\]. If we put 3 for
\[x\] and 4 for
\[y\], does it work out?

yes it does

Hmm, let's check that. If we put
\[x = 3\] into
\[y = -8x - 3\], what do we get for
\[y\]?

-27

That's right! But we got -27, not 4. So, (3,4) does not fit the first line. Do you see why?

no

That's okay! We put
\[x = 3\] into
\[y = -8x - 3\] and got
\[y = -27\], not
\[y = 4\]. So, (3,4) doesn't fit. Does that make sense?

yes

Great! So, to solve this type of problem, we:

Plug the point into both equations.
If it works for both, it's a solution. If not, it isn't.
Ready to try another problem?

what about the second equation

Good point! But since (3,4) didn't fit the first line, we know it can't be a solution for both. So, it's not a solution for the system. Does that make sense?

yes
"""

que3 = "Does the system of equation y=-8x-3 has (3, 4) as a solution?"
ans3 = "No"


### Conversation 4
conv4 = conversation_string = """
give me a system of equations question to practice

Sure thing! Let's try this one:

Liam has twice as many apples as Noah. Together, they have 18 apples. How many apples does each person have?

Remember, we need to find two equations from this problem. Can you tell me what they are?

no, can you help me

Absolutely! Let's break it down.

First, let's say Liam has
\[L\] apples and Noah has
\[N\] apples.

From the problem, we know two things. Can you tell me what those two things are?

i dont know

No worries! Let's think about it together.

The problem says Liam has twice as many apples as Noah. How can we write that as an equation using
\[L\] and
\[N\]?

The problem also says together, they have 18 apples. How can we write that as an equation using
\[L\] and
\[N\]?

N = 2L

Good start! Can you explain how you got
\[N = 2L\]? Remember, the problem says Liam has twice as many apples as Noah.

Liam has twice as many apples so it should be N = 2L

Hmm, let's think about this. If Liam has twice as many apples as Noah, wouldn't it be
\[L = 2N\]? Can you explain why you think it should be
\[N = 2L\]?

i see

Great! So we have our first equation,
\[L = 2N\]. Now, what about the second piece of information from the problem? They together have 18 apples. How can we write that as an equation using
\[L\] and
\[N\]?

l + n = 18

Fantastic! You've got it. So our two equations are
\[L = 2N\] and
\[L + N = 18\]. Now, can you solve this system of equations to find out how many apples Liam and Noah each have?

3N = 18

Great! You substituted
\[L = 2N\] into the second equation
\[L + N = 18\] to get
\[3N = 18\]. Now, what's the next step to find the value of
\[N\]?

N = 18/3 = 4

Excellent! You've found that Noah has 4 apples. Now, can you use this information to find out how many apples Liam has? Remember, Liam has twice as many apples as Noah.

L = 2*4 = 8

Bravo! You've got it. Liam has 8 apples and Noah has 4 apples. Well done on solving this system of equations!

Do you want to try another problem or is there something else you'd like to learn?
"""

que4 = "Liam has twice as many apples as Noah. Together, they have 18 apples. How many apples does each person have?"
ans4 = "Liam = 8, Noah = 4"

system_message_khanamigo = """You are a helpful AI information extractor that extracts the conversation, specifically the question and answer from the conversation between an elementary school student and a tutor.\
Think step by step

Please output in the following json format:

############# OUTPUT ############
{"Conversation": "Conversation here"
"Question": "What question is the conversation engaging in?"
"Answer": "Answer given by the tutor"}
############ OUTPUT #############

Some examples of answers corresponding to elementary math questions are:

{few_shot_examples}

Question: {input}"""

few_shot_examples_khanamigo = [{"question": f"{conv1}", "answer": f"Question:{que1} \n Answer:{ans1}"},
                     {"question": f"{conv2}", "answer": f"Question: {que2} \n Answer: {ans2}"},
                     {"question": f"{conv3}", "answer": f"Question: {que3} \n Answer: {ans3}"},
                      {"question": f"{conv4}", "answer": f"Question: {que4} \n Answer: {ans4}"}
                               ]

