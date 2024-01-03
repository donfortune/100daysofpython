# Introduction to Test Driven Development in Python

Test-Driven Development (TDD) is a software development approach where you write tests for your code before you write the actual code. The cycle typically follows these steps: write a test, run the test (it should fail because the code isn't written yet), write the code, and run the test again (it should pass this time). TDD helps ensure that your code meets the requirements and remains functional as it evolves.

As stated above, the following steps are involved in TDD:
* Write the test
* Run the test -> should fail, beacuse there is no code
* Write the code
* Run the code again -> should work since you now have the code

Test-Driven Development (TDD) in Python typically involves using testing frameworks and libraries to create and run tests. Here are some popular testing modules and libraries used for TDD in Python:
* Unittest
* Pytest
* Nose2
* Doctest
* Hypothesis
* Mock

Testing in software development can be grouped into two main categories:
1. Functional Tests
2. Non-functional Tests

Functional Tests: 
The goal of this test is to verify that the software functions as expected according to the specified requirements. The application is tested by providing input and then the results are examined that need to conform to the functionality it was intended for.
                                                    Types of Functional Tests
1. Unit Test: 
This type of testing is performed by developers before the setup is handed over to the testing team to formally execute the test cases. Unit testing is performed by the respective developers on the individual units of source code assigned areas.

The goal of unit testing is to isolate each part of the program and show that individual parts are correct in terms of requirements and functionality.

Limitations of Unit Testing:

Testing cannot catch each and every bug in an application. It is impossible to evaluate every execution path in every software application. The same is the case with unit testing.
There is a limit to the number of scenarios and test data that a developer can use to verify a source code. After having exhausted all the options, there is no choice but to stop unit testing and merge the code segment with other units.

2.Integration  Test:
Integration testing is defined as the testing of combined parts of an application to determine if they function correctly. Integration testing can be done in two ways: Bottom-up integration testing and Top-down integration testing.

Bottom-up integration: This testing begins with unit testing, followed by tests of progressively higher-level combinations of units called modules or builds.
Top-down integration: In this testing, the highest-level modules are tested first and progressively, lower-level modules are tested thereafter.
In a comprehensive software development environment, bottom-up testing is usually done first, followed by top-down testing. The process concludes with multiple tests of the complete application, preferably in scenarios designed to mimic actual situations.

3.System Testing:
System testing tests the system as a whole. Once all the components are integrated, the application as a whole is tested rigorously to see that it meets the specified Quality Standards. This type of testing is performed by a specialized testing team.

System testing is important because of the following reasons:

System testing is the first step in the Software Development Life Cycle, where the application is tested as a whole.
The application is tested thoroughly to verify that it meets the functional and technical specifications.
The application is tested in an environment that is very close to the production environment where the application will be deployed.
System testing enables us to test, verify, and validate both the business requirements as well as the application architecture.

4.Regression Testing:
Whenever a change in a software application is made, it is quite possible that other areas within the application have been affected by this change. Regression testing is performed to verify that a fixed bug hasn’t resulted in another functionality or business rule violation. The intent of regression testing is to ensure that a change, such as a bug fix should not result in another fault being uncovered in the application.

Regression testing is important because of the following reasons:

Minimize the gaps in testing when an application with changes made has to be tested.
Testing the new changes to verify that the changes made did not affect any other area of the application.
Mitigates risks when regression testing is performed on the application.
Test coverage is increased without compromising timelines.
Increase speed to market the product.

5.Acceptance Testing:
This is arguably the most important type of testing, as it is conducted by the Quality Assurance Team who will gauge whether the application meets the intended specifications and satisfies the client’s requirement. The QA team will have a set of pre-written scenarios and test cases that will be used to test the application.

More ideas will be shared about the application and more tests can be performed on it to gauge its accuracy and the reasons why the project was initiated. Acceptance tests are not only intended to point out simple spelling mistakes, cosmetic errors, or interface gaps, but also to point out any bugs in the application that will result in system crashes or major errors in the application.

By performing acceptance tests on an application, the testing team will deduce how the application will perform in production. There are also legal and contractual requirements for acceptance of the system.

# Alpha Testing
This test is the first stage of testing and will be performed amongst the teams (developer and QA teams). Unit testing, integration testing and system testing when combined together is known as alpha testing. During this phase, the following aspects will be tested in the application:

Spelling Mistakes
Broken Links
Cloudy Directions
The Application will be tested on machines with the lowest specification to test loading times and any latency problems.

# Beta Testing
This test is performed after alpha testing has been successfully performed. In beta testing, a sample of the intended audience tests the application. Beta testing is also known as pre-release testing. Beta test versions of software are ideally distributed to a wide audience on the Web, partly to give the program a “real-world” test and partly to provide a preview of the next release. In this phase, the audience will be testing the following:

Users will install, run the application and send their feedback to the project team.
Typographical errors, confusing application flow, and even crashes.
Getting the feedback, the project team can fix the problems before releasing the software to the actual users.
The more issues you fix that solve real user problems, the higher the quality of your application will be.
Having a higher-quality application when you release it to the general public will increase customer satisfaction.

Non-functional Tests:
Non-functional testing is a type of software testing that assesses aspects of the software that are not related to specific behaviors or functions. Instead, it focuses on attributes such as performance, reliability, usability, and security.
                                                    Types of Non-Functional Tests
1.Performance Testing:
It is mostly used to identify any bottlenecks or performance issues rather than finding bugs in a software. There are different causes that contribute in lowering the performance of a software:

Network delay
Client-side processing
Database transaction processing
Load balancing between servers
Data rendering
Performance testing is considered as one of the important and mandatory testing type in terms of the following aspects:

Speed (i.e. Response Time, data rendering and accessing)
Capacity
Stability
Scalability
Performance testing can be either qualitative or quantitative and can be divided into different sub-types such as:
(a) Load testing 
(b) Stress testing.

(a)Load Testing:
It is a process of testing the behavior of a software by applying maximum load in terms of software accessing and manipulating large input data. It can be done at both normal and peak load conditions. This type of testing identifies the maximum capacity of software and its behavior at peak time.

Most of the time, load testing is performed with the help of automated tools such as Load Runner, AppLoader, IBM Rational Performance Tester, Apache JMeter, Silk Performer, Visual Studio Load Test, etc.

Virtual users (VUsers) are defined in the automated testing tool and the script is executed to verify the load testing for the software. The number of users can be increased or decreased concurrently or incrementally based upon the requirements.

(b)Stress Testing:
Stress testing includes testing the behavior of a software under abnormal conditions. For example, it may include taking away some resources or applying a load beyond the actual load limit.

The aim of stress testing is to test the software by applying the load to the system and taking over the resources used by the software to identify the breaking point. This testing can be performed by testing different scenarios such as:

Shutdown or restart of network ports randomly
Turning the database on or off
Running different processes that consume resources such as CPU, memory, server, etc.

2.Usability Testing:
Usability testing is a black-box technique and is used to identify any error(s) and improvements in the software by observing the users through their usage and operation.

Usability can be defined in terms of five factors, i.e. efficiency of use, learn-ability, memory-ability, errors/safety, and satisfaction. the usability of a product will be good and the system is usable if it possesses the above factors.

usability is the quality requirement that can be measured as the outcome of interactions with a computer system. This requirement can be fulfilled and the end-user will be satisfied if the intended goals are achieved effectively with the use of proper resources.

a user-friendly system should fulfill the following five goals, i.e., easy to Learn, easy to remember, efficient to use, satisfactory to use, and easy to understand.

3.Security Testing:
Security testing involves testing a software in order to identify any flaws and gaps from security and vulnerability point of view. Listed below are the main aspects that security testing should ensure:

Confidentiality
Integrity
Authentication
Availability
Authorization
Non-repudiation
Software is secure against known and unknown vulnerabilities
Software data is secure
Software is according to all security regulations
Input checking and validation
SQL insertion attacks
Injection flaws
Session management issues
Cross-site scripting attacks
Buffer overflows vulnerabilities
Directory traversal attacks

4.Portability Testing:
Portability testing includes testing a software with the aim to ensure its reusability and that it can be moved from another software as well. Following are the strategies that can be used for portability testing:

Transferring an installed software from one computer to another.
Building executable (.exe) to run the software on different platforms.
Portability testing can be considered as one of the sub-parts of system testing, as this testing type includes overall testing of a software with respect to its usage over different environments. Computer hardware, operating systems, and browsers are the major focus of portability testing. Some of the pre-conditions for portability testing are as follows:

Software should be designed and coded, keeping in mind the portability requirements.
Unit testing has been performed on the associated components.
Integration testing has been performed.
Test environment has been established.

# Now that we have an understanding of the different types of Testing and when to use which. lets now look at planning tests:
A test plan outlines the strategy that will be used to test an application, the resources that will be used, the test environment in which testing will be performed, and the limitations of the testing and the schedule of testing activities. Typically the Quality Assurance Team Lead will be responsible for writing a Test Plan.

A test plan includes the following:

Introduction to the Test Plan document
Assumptions while testing the application
List of test cases included in testing the application
List of features to be tested
What sort of approach to use while testing the software
List of deliverables that need to be tested
The resources allocated for testing the application
Any risks involved during the testing process
A schedule of tasks and milestones to be achieved
Test Scenario
It is a one line statement that notifies what area in the application will be tested. Test scenarios are used to ensure that all process flows are tested from end to end. A particular area of an application can have as little as one test scenario to a few hundred scenarios depending on the magnitude and complexity of the application.

The terms ‘test scenario’ and ‘test cases’ are used interchangeably, however a test scenario has several steps, whereas a test case has a single step. Viewed from this perspective, test scenarios are test cases, but they include several test cases and the sequence that they should be executed. Apart from this, each test is dependent on the output from the previous test.

Test Case
Test cases involve a set of steps, conditions, and inputs that can be used while performing testing tasks. The main intent of this activity is to ensure whether a software passes or fails in terms of its functionality and other aspects. There are many types of test cases such as functional, negative, error, logical test cases, physical test cases, UI test cases, etc.

Furthermore, test cases are written to keep track of the testing coverage of a software. Generally, there are no formal templates that can be used during test case writing. However, the following components are always available and included in every test case:

Test case ID
Product module
Product version
Revision history
Purpose
Assumptions
Pre-conditions
Steps
Expected outcome
Actual outcome
Post-conditions
Many test cases can be derived from a single test scenario. In addition, sometimes multiple test cases are written for a single software which are collectively known as test suites.
