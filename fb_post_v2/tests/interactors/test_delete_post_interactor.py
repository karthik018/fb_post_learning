from unittest.mock import Mock
import unittest

from fb_post_v2.interactors.delete_post_interactor import DeletePostInteractor
from fb_post_v2.interactors.storages.post_storage import PostStorage
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter

class TestDeletePos(unittest.TestCase):
    def test_delete_post(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        delete_post = DeletePostInteractor(post_storage_mock, presenter_mock)

        post_id = 1
        response_data = {"status": "post deleted"}

        post_storage_mock.post_exists.return_value = True
        post_storage_mock.delete_post.return_value = response_data
        presenter_mock.delete_post.return_value = response_data
        response = delete_post.delete_post(post_id)

        post_storage_mock.delete_post.assert_called_once_with(post_id)
        presenter_mock.delete_post.assert_called_once_with(response_data)
        assert response == response_data

    def test_post_not_exists(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        delete_post = DeletePostInteractor(post_storage_mock, presenter_mock)

        post_id = 2
        response_data = {"response": "post does not exists"}

        post_storage_mock.post_exists.return_value = False
        presenter_mock.post_not_exists.return_value = response_data
        response = delete_post.delete_post(post_id)

        post_storage_mock.post_exists.assert_called_once_with(post_id)
        presenter_mock.post_not_exists.assert_called_once()
        assert response == response_data

