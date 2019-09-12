**What challenges did you encounter with this assignment, if any?**

I feel there can be bugs when using float point numbers but I could find a strategy to test it out.
 
**What did you think about the requirements specification for this assignment?**

The requirements specification is not clear enough:
1. It doesn't state what is the type of the inputs. Can it be float? Is integer strings are allowed?
2. It doesn't talk about the case of not a valid triangle. i.e. `a >= b + c`.
3. It doesn't state the required accuracy of the application. 

Due to the ambiguous specification, I took the following decisions for each of these point:
1. Program accepts only integer and float variables and throws error otherwise.
2. Program raises an exception if the given parameters doesn't represent a valid triangle.
3. The accuracy of the application is up to 1e-10.

**What challenges did you encounter with the tools?**

I didn't face any problems with tool. It was easy to use and straight forward for this example.

**Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?**
- Code coverage. I made sure to have 100% code coverage for test case.
- Tried some extreme cases. Like big integer number or float with fine float point.
- Tried some edge case. Like for showing error when `a >= b + c`, I tested one case when `a = b + c` and another when `a > b + c`.
- In case I have condition with `or`, I tried to write test case for each term.


**Known Bugs:**

There is a bug that left intentionally in the code: Isosceles triangle is not returned if `a == c`.