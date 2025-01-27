# anonymize-initials

## How Does It Work?

There is no way to deanonmyize the initials as they arereplaced by random initials. The only ways to do so are: guess from context; save the output of print function. The output of print function is also valid YAML which can be further converted to JSON, or any other format.

The script will take care itself of these conditions: the result is not same as key; the result is not "I"; the result is a char with values ranging from 65-90[A-Z]. You will have to handle collisions yourself.

## Usage

To use this program, populate the `orignal_initials` tuple with the initials you want to anonmyize. While it is an tuple, consider it to be a **const set of chars**. It is recommended to only use upper case letters.

Example in C++ because Python does not have char: ```const std::set<char> original_initials = {'A', 'B', 'C'};```


Lets take a real life example. Below is a conversation from my Fanclub, as discussed in my [memoir](https://hstsethi.vercel.app/posts/lifestyle/lessons-learned-founding-internet-groups-memoir). Here the initials are alreadyanonymized, but we will do that again.

The original conversation:

```
A: unfortunately using windows disqualifies your opinion from being considered. B: yea sure ok T: one day you will switch to free because not even you could bear the windows of future Me: Windows user opinion don't count. I won as always
```

Collecting initials from the conversation and running script, with `python src/get-anonymized-initials.py > lessons-initials.yml`, we get:

```
A: Y
T: L
B: W
```

Now we can simply subsistute them with `tr`, as it will be most efficent, even more than sed. Additionally, the result YAML be converted to JSON, encrypted with GPG.

Another way would be to create a dictionary of the results. Then pass that to replace function, however that would be less efficient and can cause collisions of values, not of keys, as dictionary doesn't allow duplicate keys.
