def test_align_tensors():
    # test for three matrices

    matrix = tl.tensor([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0.1, 0, 0, 0], [0, 0, 1, 0, 0],
                        [0, 0, 0, 0.5, 1]])
    order_hat = align_tensors(matrix)
    true_order = tl.tensor([0, 1, 3, 2, 4])
    assert_equal(order_hat, true_order)

    matrix = tl.tensor([[0, 1, 0, 0], [1, 0, 0.5, 0], [0.5, 0, 1, 0.3], [0, 0, 0.2, 0.3]])
    order_hat = align_tensors(matrix)
    true_order = tl.tensor([1, 0, 2, 3])
    assert_equal(order_hat, true_order)

    matrix = tl.tensor([[0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0.3, 0, 1], [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0]])
    order_hat = align_tensors(matrix)
    true_order = tl.tensor([1, 4, 0, 3, 2])
    assert_equal(order_hat, true_order)


def test_factor_match_score_3d():
    # same factors
    X_true = KruskalTensor((tl.tensor([1, 2]), [tl.tensor([[4, 1], [0, 2]]),
                                                tl.tensor([[0, 1], [3, 5]]),
                                                tl.tensor([[1, 1], [1, 2]])]))
    Y_true = KruskalTensor((tl.tensor([1, 1]), [tl.tensor([[4, 1], [0, 2]]),
                                                tl.tensor([[1, 1], [1, 2]])]))
    assert_array_almost_equal(1, factor_match_score_3d(X_true, Y_true, X_true, Y_true))

    # with permutation and scaling and sign
    X_pred = KruskalTensor((tl.tensor([2 * np.sqrt(650), -np.sqrt(288)]),
                            [tl.tensor([[1 / np.sqrt(5), -1], [2 / np.sqrt(5), 0]]),
                             tl.tensor([[1 / np.sqrt(26), 0], [5 / np.sqrt(26), 1]]),
                             tl.tensor([[1 / np.sqrt(5), 1 / np.sqrt(2)],
                                        [2 / np.sqrt(5), 1 / np.sqrt(2)]])]))
    Y_pred = KruskalTensor((tl.tensor([-5, -4*np.sqrt(2)]),
                            [tl.tensor([[1 / np.sqrt(5), -1], [2 / np.sqrt(5), 0]]),
                             tl.tensor([[-1 / np.sqrt(5), 1 / np.sqrt(2)],
                                        [-2 / np.sqrt(5), 1 / np.sqrt(2)]])]))
    assert_array_almost_equal(1, factor_match_score_3d(X_true, Y_true, X_pred, Y_pred))