##### Write a script that uses the randint() function to simulate the toss of a die, returning a random number between 1 and 6

##### Write a script that simulates 10,000 throws of dice and displays the average number resulting from these tosses

##### Write a script “election.py” that will simulate an election between two candidates, A and B. One of the candidates wins the overall election by a majority based on the outcomes of three regional elections. (In other words, a candidate wins the overall election by winning at least two regional elections.)
    Candidate A has the following odds:
    - 87% chance of winning region 1
    - 65% chance of winning region 2
    - 17% chance of winning region 3
Import and use the random() function from the random module to simulate events based on probabilities; this function doesn't take any arguments (meaning you don't pass it any input variables) and returns a random value somewhere between 0 and 1.
Simulate 10,000 such elections, then (based on the average results) display the probability that Candidate A will win and the probability that Candidate B will win.

##### Write a script “poetry.py” that will generate a poem based on randomly chosen words and a pre-determined structure. When you are done, you will be able to generate poetic masterpieces such as the following in mere milliseconds:
    A furry horse
    A furry horse curdles within the fragrant mango extravagantly, the horse slurps the mango meows beneath a balding extrovert

All of the poems will have this same general structure, inspired by Clifford Pickover:
```
{A/An} {adjective1} {noun1}
{A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
{adverb1}, the {noun1} {verb2} the {noun2} {verb3} {preposition2} a {adjective3} {noun3}
```

Your script should include a function makePoem() that returns a multi-line string representing a complete poem. The main section of the code should simply print makePoem() to display a single poem. In order to get there, use the following steps as a guide:
- First, you’ll need a vocabulary from which to create the poem. Create several lists, each containing words pertaining to one part of speech (more or less); i.e., create separate lists for nouns, verbs, adjectives, adverbs, and prepositions. You will need to include at least three different nouns, three verbs, three adjectives, two prepositions and one adverb. You can use the sample word lists below, but feel
free to add your own:

    Nouns: "fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"

    Verbs: "kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"

    Adjectives: "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"

    Prepositions: "against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"

    Adverbs: "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"

- Choose random words from the appropriate list using the random.choice() function, storing each choice in a new string. Select three nouns, three verbs, three adjectives, one adverb, and two prepositions. Make sure that none of the words are repeated. (Hint: Use a while loop to repeat the selection process until you get a
new word.)

- Plug the words you selected into the structure above to create a poem string by
using the format() string method
- Bonus: Make sure that the “A” in the title and the first line is adjusted to become
an “An” automatically if the first adjective begins with a vowel.