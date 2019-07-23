from fb_post_v2.interactors.storages.post_storage import TotalReactionDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestTotalReactionCount:

    def test_total_reaction_count(self):
        presenter = JsonPresenter()

        count_dto = TotalReactionDTO(count=2)

        response = presenter.get_total_reaction_count(count_dto)

        assert response["total_count"] == count_dto.count

class
