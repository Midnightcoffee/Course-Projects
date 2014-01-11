/*
 * =====================================================================================
 *
 *       Filename:  project.cpp
 *
 *    Description: infix to postfix and evaluate
 *
 *        Version:  1.0
 *        Created:  03/13/2013 01:55:51 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Drew Verlee (access id:fd4544), fd4544@wayne.edu
 *   Organization:  ka-tet
 *
 * =====================================================================================
 */
#include <cassert>
#include <iostream>
#include <stack>
#include <fstream>
#include <iomanip>
#include <queue>
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::stack;
using std::ifstream;
using std::setw;
using std::queue;

bool isBalanced(const string& expression);
string infixToPostfix(const string& expression);
double evaluatePostfix(const string& expression);
queue<string> readIn(string fileName );
void testEvaulatePostfix();
void testInfixToPostfix();
void testIsbalanced();
void testReadIn();

 /* ======================================================================
 *      Method     : Main
 *      Description:  Will read in a infix expression from a text file,
 *      check if the parentheses in the input expression are balanced,
 *      convert the infix expression into a postfix expression, and evaluate
 *      the expression
 * =====================================================================*/

int main()
{
    string expression;
    string postfixExpression;
    double result;

    /* test plan:
    * These functions are the testing "procedure". I "believe" the
     * program works because the tests pass and all the expressions evaluate,
     correctly.*/
    testIsbalanced();
    testInfixToPostfix();
    testEvaulatePostfix();
    testReadIn();

    /* Design plan:
     * create algorithms for balance, infix to postfix, evaluate and read in.
     *  balance - keep record of open parens and close parens in stack
     *  infix to postfix - read expression into stack, push and pop depending one
     *      operator or operand
     *  evaluate postfix - read expression into stack, push and pop depending 
     *  operator precedence.
     *  read in - enqueue lines into a queue, as to maintain order
     *  main - link functions together.
     * check that arguments and returns flow from one function to another.
     * implement algorithms in psuedo code
     * write tests in python
     * code to pass tests in python
     * rewrite code in c++
     * */

    cout << endl;
    cout << "** test project *************"  << endl;

    queue<string> expressions = readIn("expressions.txt");
    cout << setw(12) << "prefix" << setw(12) << "postfix" << setw(12)<< "result" << endl;
    while(!expressions.empty()){
        expression = expressions.front();
        expressions.pop();
        if(isBalanced(expression)){
            postfixExpression = infixToPostfix(expression);
            result = evaluatePostfix(postfixExpression);
            cout << setw(12) << expression << setw(12) << postfixExpression
                << setw(12) << result << endl;
        }
        else{
            cout << setw(12) << expression << setw(12) <<
                setw(16) << "not balanced" << endl;
        }
    }
    cout << " ** test project pass **********" << endl << endl;

    /* Results of test project: */
    /* ** test project ************* */
    /*       prefix     postfix      result */
    /*        (1+1)         11+           2 */
    /*        (1+2)         12+           3 */
    /*      (1*3)+1       13*1+           4 */
    /*  (1+1)*(2*2)     11+22**           8 */
    /*    ((1+2)*2)       12+2*           6 */
    /*          1+1         11+           2 */
    /*          2*2         22*           4 */
    /*           ((   not balanced */
    /*           ))   not balanced */
    /*         1+1)   not balanced */
    /*  ** test project pass ********** */

    return 0;

}

 /* ======================================================================
 *            Method: isBalanced
 *      Description : checks to see if parentheses are balanced
 * =====================================================================*/
bool isBalanced(const string& expression)
{
    stack<char> openParens;
    for (unsigned int i = 0; i < expression.length(); i++) {
        if(expression[i] == '('){
            openParens.push(expression[i]);
        } else if(expression[i] == ')'){
            if(openParens.empty()){ /* encounter a close with no open? */
                return false;
            }
            else{
                openParens.pop(); /* if we match we just empty the stack*/
            }
        }
        else{
            /* do nothing, this is reserved for operators and operands */
        }
    }
    if(openParens.empty()){ /* an empty list means no left over parens */
        return true;
    }
    else{
        return false;
    }
}

 /* ======================================================================
 *            Class: testIsbalanced
 *      Description: tests isBalanced
 * =====================================================================*/
void testIsbalanced()
{
    bool solution;
    bool output;

    cout << endl;
    cout << "** test isBalanced *****************"  << endl;
    /* is balanced tests */

    cout <<  " output " <<  setw(11) << "solution " << endl;

    output = isBalanced(""); solution = true;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("()"); solution = true;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("(("); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("("); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced(")"); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced(")("); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("(())"); solution = true;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("()()"); solution = true;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("()("); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("a"); solution = true;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("(a)"); solution = true;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("(a))"); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("(a))("); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = isBalanced("(a))("); solution = false;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    cout << "** test isBalanced pass *************"  << endl;
}
 /* ======================================================================
 *      Method     : infixToPostfix
 *      Description: given a infix expression, returns a postfix
 * =====================================================================*/
string infixToPostfix(const string& expression)
{
    stack<int> s; /* s holds elements tell we can add them to our postfixExpression*/
    string postfixExpression;   /* result, holds the postfix expression were building */
    string prec = "(+*";
    string numbers = "0123456789"; /* used to check if char contains int */
    char element; /* of an expression*/
    int checker;
    char top;

    for(unsigned int i = 0; i < expression.length(); i++) {
        element = expression[i]; /* e  */
        checker = numbers.find(element); /* assigns p to -1 if its not a int, so (+* */
        if(checker != -1){
            postfixExpression += element;
        } else if(element == '('){
            s.push(element);
        } else if(element == ')'){
            top = s.top();
            s.pop();
            while(top != '('){/* search tell we get a open paren */
                postfixExpression += top;
                top = s.top();
                s.pop();
            }
        }
        else{
            /* reorder our expression based on operator rank */
            while(!s.empty() && (prec.find(s.top()) >= prec.find(element))){
                postfixExpression += s.top();
                s.pop();
            }
            s.push(element);
        }
    }
    while(!s.empty()){
        postfixExpression += s.top();
        s.pop();
    }
    return postfixExpression;
}
 /* ======================================================================
 *            Method: testInfixToPostfix
 *      Description: test for infixToPostfix
 * =====================================================================*/
void testInfixToPostfix()
{
    cout << endl;
    cout << "** test infixToPostfix *************"  << endl;
    string output;
    string solution;

    cout <<  " output " <<  setw(11) << "solution " << endl;

    output = infixToPostfix("");
    solution = "";
    assert(output == solution);

    output = infixToPostfix("1");
    solution = "1";
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = infixToPostfix("1+1");
    solution = "11+";
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = infixToPostfix("(1+1)");
    solution = "11+";
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = infixToPostfix("((2+3)*(1+5))");
    solution = "23+15+*";
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = infixToPostfix("(1+(2+(3+4)))");
    solution = "1234+++";
    assert(output == solution);
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;

    cout << "** test infixToPostfix pass ************"  << endl;
}

 /* ======================================================================
 *            Method: evaluatePostfix
 *      Description: evaluates expressions in postfix notation
 * =====================================================================*/
double evaluatePostfix(const string& expression)
{
    string prec = "+*";
    string numbers = "0123456789";
    stack<int> operands; /* holds our elements */
    double result;
    char element;
    int operand;
    int t1; /* top item in stack */
    int t2; /*given a t1, the next item */
    for (unsigned int i = 0; i < expression.length(); i++) {
        element = expression[i];
        operand = numbers.find(element); /* assigns p to -1 if not found */
        if(operand != -1){ /* if operand add to stack*/
            operands.push(operand);
        }
        else{ /* else if operator */
            result = 0;
            t1 = operands.top();
            operands.pop();
            t2 = operands.top();
            operands.pop();
            if(element == '+'){/* pop off the top two and operate on them */
                result += (t1 + t2);
            }
            else{
                result += (t1 * t2);
            }
            operands.push(result);/* store that result */
        }
    }
    return operands.top();
}
 /* ======================================================================
 *          Method : testEvaulatePostfix
 *      Description: tests evaluate function.
 * =====================================================================*/
void testEvaulatePostfix()
{
    double output;
    double solution;

    cout << endl;
    cout << "** test EvaulatePostfix  ***********"  << endl;

    cout <<  " output " <<  setw(11) << "solution " << endl;


    output = evaluatePostfix("11+");
    solution = 2;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);

    output = evaluatePostfix("12+2*");
    solution = 6;
    cout <<  setw(8) << output << setw(2) << "|" << setw(8) << solution  << endl;
    assert(output == solution);


    cout << "** test EvaulatePostfix pass ***********"  << endl;
}
 /* ======================================================================
 *            Method: ReadIn;
 *      Description:  given a filename, returns a lines
 * =====================================================================*/
queue<string> readIn(string fileName )
{

    string line;
    queue<string> expressions;
    ifstream in_file((fileName).c_str());/* c_str allows us to enter a string */

    if(in_file.is_open()){
        while(!in_file.eof()){
            getline(in_file, line, '\n');
            if(line != ""){
                expressions.push(line);
            }
        }
        in_file.close();
    }
    else{
        cout << "unable to open" << endl;
    }
    return expressions;
}

 /* ======================================================================
 *            Method: testReadIn;
 *      Description: tests readIn function
 * =====================================================================*/
void testReadIn()
{
    string solution;
    queue<string> output;
    cout << endl;
    cout << "** test readIn *************"  << endl;

    cout <<  " output " <<  setw(14) << "solution " << endl;
    output  = readIn("test1.txt");
    solution = "(1+2)*(1+1)";
    cout <<  setw(12) << output.front() << setw(2) << " | " << setw(8) << solution  << endl;
    assert(output.front() == solution);
    output.pop();

    output  = readIn("test2.txt");
    solution = "(1+1)";
    cout <<  setw(12) << output.front() << setw(2) << " | " << setw(8) << solution  << endl;
    assert(output.front() == solution);
    output.pop();
    solution = "2+2";
    cout <<  setw(12) << output.front() << setw(2) << " | " << setw(8) << solution  << endl;

    cout << "** test readIn pass *************"  << endl;
}
