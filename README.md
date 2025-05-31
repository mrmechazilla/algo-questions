# Algorithm Questions Documentation


## Approaches

#### 1. Dynamic programming

A way to solve problems by breaking them into smaller subproblems and reusing their results to save time. It can be broken down into 3 steps:

1. Break the problem into smaller comparisons (e.g. character by character).
2. Store the result of each comparison in a table (called dp) so we don’t recalculate it again.
3. Efficiently build up to the final solution using already computed values.



## How to handle API problems

I mainly use FASTAPI.

for FASTAPI apps run this command inside the venv to start the server:  uvicorn upload_json:app --reload

:construction: Work in progress