function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
% nn parms is being used when passed to function
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%

 % DREWS CODE STARTS HERE -------

% create the y matrix, logic from discussion forums
y = repmat(1:num_labels, size(y,1) , 1) == repmat(y, 1, num_labels);

% add a column of 1's to the X matrix
row_size_of_x = size(X, 1);
column_of_ones_x = ones(row_size_of_x, 1);
% append it to front of X matrix
a1 = [column_of_ones_x, X];
% ------------ compute hidden layers -------------------

z2 = a1 * transpose(Theta1); % try X * Theta1 Transpose
a2 = sigmoid(z2);

% add a column of 1's to the a2 5000x25 matrix
row_size_of_a2 = size(a2, 1);
column_of_ones_a2 = ones(row_size_of_x, 1);
% append it to the front of a2 matrix
a2 = [column_of_ones_a2, a2];

% compute output layer/hypothesis
z3 = a2 * transpose(Theta2);
a3 = sigmoid(z3);
hypothesis = a3;

% ------------- end hidden layers ------------

% compute our matrix of cost values should mirror idea in link
% https://class.coursera.org/ml-004/forum/thread?thread_id=2435

% Difference from logistic function
% Change "*" to ".*" ::: that is you want element wise multiplication between y and X
% Change y' to y ::: that is remove the tranpose from y because you want element wise subtraction
J_matrix = (( (1/m) ) * ((-y .* log(hypothesis)) - ((1 - y) .* log(1 - hypothesis))));

% sum them over rows should create a (labels * 1) vector of costs
sum_over_rows = sum(J_matrix, 2);
% sum over column to get our final cost function
J = sum(sum_over_rows);

% ------------- reached end of output layer -------------
% -------------- this reaches end of submit 1 -------------
% -------------- NICE WORK -------------------------

% ------------- 1.4 Regularized cost function -- part 2 -----------

% don't select the first column/bias value

T1 = Theta1(1:end, 2:end);
T2 = Theta2(1:end, 2:end);

T1_summed = sum(sum(T1.^2));
T2_summed = sum(sum(T2.^2));


reg = ((lambda/(2 * m)) * (T1_summed + T2_summed));
J = J + reg;

% ------------- end regularization -- part 2 -----------------------
% ------------- Nice work ---------------


% -------------- end cost function ------------------


% notes like this are from original doc..
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% --------------------- vector-back try/ 2.3 /  --------------
% recall this (our matrices) is by rows as opposed to professors which are by 
% columns

% a1 =          5000,401
% a2 =          5000,26
% a3 =          5000,10
% y =           5000, 10
% Theta1 =      25, 401
% Theta2 =      10, 26
% T1 =          5000,25
% T2 =          10,25

% for back prob
%delta3 =       5000, 10
%partial_derv = 5000, 25

% -----------------
% first_term = 5000,26
% delta2 = 26,10

% you can throw element out at start or at end.
% example with 10 [ 0...., 1] - [...... %chance to be a 1]
delta3 = a3 - y; % this makes sense

% dont mult with bias rows 
% RELABLE
%5000,25 =     (5000 * 10) * (10,25) <- point of confusion .. Because it needs to be final same size as a2
first_term  = (delta3 * T2);

% 5000, 25
partial_derv = sigmoidGradient(z2);

% have to arrange these so numbers work out/ logic :(

% should be element wise multiplication. (want d2 to be 5000, 26)
% this is step three in the assignment 
% (5000, 25)  =     (5000, 25) * (5000, 25) /// want to be the same as a2
delta2 = first_term .* partial_derv ;

% delta2 to be the same size as our seconl layer /a2
% 26,10      =  (26, 5000) * (5000,10)


% trying to throw out at end...
% possible trying to calculate gradient?
DELTA_2 = (delta3' * a2);
%         5000,401  (25,10)
DELTA_1 = (delta2' * a1);


% finished step 4 next step is dividing delta2 matrix by m
% .. then divid my m
% commented out for regularization
%DELTA_2 = DELTA_2 / m;
%DELTA_1 = DELTA_1 / m;
%% finished step 5
%
%Theta1_grad = DELTA_1;
%Theta2_grad = DELTA_2;

% ---------------- end submit part 4 Neural network graident (backpropagation) 

% ---------------------- 2.5 REGULARIZATION Neural Network start --------



% DELTA_L with j = 0 is DELTA = 1/m * DELTA_L 
% DELTA_L with j !=0 is DELLTA_L = 1/m DELTA_L + lamba/m * theta?
DELTA_2 = [DELTA_2(:,1) * (1/m), (DELTA_2(1:end, 2:end) * (1/m)) + ((lambda/m) .* T2) ];
DELTA_1 = [DELTA_1(:,1) * (1/m), (DELTA_1(1:end, 2:end) * (1/m)) + ((lambda/m) .* T1)];

Theta1_grad = DELTA_1;
Theta2_grad = DELTA_2;

% ---------------------- 2.5 REGULARIZATION Neural Network end --------
% --------------------- NICE WORK -------------------!!!

% ------------------- back prop vector try end ...------------------


% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
