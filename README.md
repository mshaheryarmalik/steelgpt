# SteelGPT is code repository for Junction 2023 Hackathon Challenge.

## Utilizing generative Artificial Intelligence in a sustainable manner to collect and summarize real time insights to help drive business decisions.

### The challenge

Your challenge, should you accept it, is to build a sustainable AI assistant for dynamic information retrieval and summarization to support business critical use cases. As Sustainable AI is a very broad topic, to keep things simple, for this challenge we would like to focus on two aspects of Sustainable AI: trustworthiness and efficiency (which we are using here as a proxy for ecological sustainability, through more limited energy use and carbon footprints). So this is not “just” about building an information retrieval assistant and feeding huge amounts of data to an enormous model – that is easy. We want you to build a system that accomplishes the same but in a very trustworthy and sustainable way, and that makes things quite a bit more challenging… so you need to work smart not just hard on how you accomplish the task, as “bruteforcing” this will not result in the desired outcome. But hey, that’s why this is called a challenge, we know you are up for it!

Trustworthiness has also a few different aspects. Firstly, it is about using the right data – as correct information as possible as the source. We all know that the internet is not necessarily always correct… so how do you know what sources to trust? But even when you have the right information, summarizing that might not always get you what you want either. One of the fairly common challenges of generative models is hallucinations, effectively inventing results to questions where there are none. This leads to a lack of trust and can even be a barrier to usage. You should strive to build a system that bases the outputs on sources you can trust and avoids hallucinations to ensure the outputs of the system are reliable and trustworthy.

Furthermore, as we know, large language models are quite resource intensive. Especially training models tends to consume large amounts of energy, but also interference (when you use the models) can be costly – especially when done at scale. As it is not in scope for this challenge to build a model from scratch, let’s focus on the computational costs related to using an existing model – both in terms of which model to choose and how we use it. This is something we can often control better in practical applications too, as even if we use existing large models, we can definitely decide which ones to use and how we use them. So while this is a very exciting set of technologies, we should use them wisely and avoid excessive resource consumption. Less is definitely more in this context – and the best solution probably does not use the biggest model or the broadest context possible (or very large amounts of queries to a model – it is the total cost that counts) – and a big part of the challenge is to optimize the resource usage while still getting great results.

This solution, if successful, can make a huge difference – and shed light on how tasks like can be accomplished in a sustainable way. So it is not just about building something very cool and useful but showcasing how thinking about of the sustainability of AI can make a real positive difference!

### Insights

As to the actual solution, we will encounter different types of questions, and ideally the solution could have quite general applicability. But since that is of course rather complex to construct, let’s focus on some example questions (note – these are not the only questions the solution should answer, just some examples to give you an idea – when evaluating your solution, we will use similar but not necessarily just these):

1. What is the expected development of stainless steel market pricing for a specific alloy in the next month?

2. What recent news state about possible energy price developments over the next three months?

3. What are the most recent patents granted in the area of stainless steel manufacturing?

For practicality, we expect the assistant to be able to connect to the internet, fetch relevant data and be able to produce well summarized results in human readable format in the range of one or two paragraphs per question – with a special focus on avoiding hallucinations and basing the results on the source information and being ecological and efficient in how this is done. The results should always include a reference to the sources of the information used to construct the answer.

The architecture should be such that the actual model component is easily interchangeable (as this is a rapidly developing field), and working from the assumption that you do not need to fine-tune or retrain the actual model, but supply the data through prompting in a way that you find most effective. And in order to evaluate your ecological consumption, we would like you to also estimate the energy impact of the query having been executed (understanding that this is just an estimate, and using the number and size of queries and size of the model used as proxy is a good approach – although we welcome you to innovate also in this front)

### Demo Video
[Let's Go!] (https://youtu.be/h27J-zgJ9Xs)

### Figma Design
[Let's Design!] (https://www.figma.com/proto/xo5YqnjV7MBPn3ZqjvXzeg/SteelGPT?page-id=0%3A1&type=design&node-id=2-2&viewport=353%2C418%2C0.06&t=bdG7tEfHzgauKbG2-1&scaling=scale-down&starting-point-node-id=38%3A3681&mode=design)