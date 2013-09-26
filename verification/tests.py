"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "((5+3)*2+1)",
            "answer": True
        },
        {
            "input": "{[(3+1)+2]+}",
            "answer": True
        },
        {
            "input": "(3+{1-1)}",
            "answer": False
        },
        {
            "input": "[1+1]+(2*2)-{3/3}",
            "answer": True
        },
        {
            "input": "(({[(((1)-2)+3)-3]/3}-3)",
            "answer": False
        },
        {
            "input": "[(3)+(-1)]*{3}",
            "answer": True
        },
        {
            "input": "(((([[[{{{3}}}]]]]))))",
            "answer": False
        },
        {
            "input": "[1+202]*3*({4+3)}",
            "answer": False
        },
        {

            "input": "({[3]})-[4/(3*{1001-1000}*3)/4]",
            "answer": True
        },
        {
            "input": "[[[1+[1+1]]])",
            "answer": False
        },
        {
            "input": "(((1+(1+1))))]",
            "answer": False
        }

    ],
    "Extra": [
        {
            "input": "[[5+3]*2+1]",
            "answer": True
        },
        {
            "input": "{([3+1]+2)+}",
            "answer": True
        },
        {
            "input": "[3+{1-1]}",
            "answer": False
        },
        {
            "input": "(1+1)+[2*2]-{3/3}",
            "answer": True
        },
        {
            "input": "[[{([[[1]-2]+3]-3)/3}-3]",
            "answer": False
        },
        {
            "input": "([3]+[-1])*{3}",
            "answer": True
        },
        {
            "input": "[[[[((({{{3}}}))))]]]]",
            "answer": False
        },
        {
            "input": "(1+202)*3*[{4+3]}",
            "answer": False
        },
        {

            "input": "[{(3)}]-(4/[3*{1001-1000}*3]/4)",
            "answer": True
        },
        {
            "input": "(((1+(1+1))))]",
            "answer": False
        }

    ]
}
