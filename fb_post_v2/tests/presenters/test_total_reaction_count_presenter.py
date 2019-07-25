from fb_post_v2.interactors.storages.post_storage import TotalReactionCountDTO, \
    ReactionCountDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestTotalReactionCount:

    def test_total_reaction_count(self):
        presenter = JsonPresenter()

        count_dto = TotalReactionCountDTO(count=2)

        response = presenter.get_total_reaction_count_response(count_dto)

        assert response["total_count"] == count_dto.count

class TestReactionMetrics:

    def test_reaction_metrics(self):
        presenter = JsonPresenter()

        count1_dto = ReactionCountDTO(count=2, reaction="LOVE")
        count2_dto = ReactionCountDTO(count=3, reaction="LIKE")

        reactions_dto = [count1_dto, count2_dto]

        response = presenter.get_reaction_metrics_response(reactions_dto)

        assert len(response["reactions"]) == len(reactions_dto)

        test_reaction = {}
        for reaction in response["reactions"]:
            if reaction["reaction"] == count1_dto.reaction:
                test_reaction = reaction

        assert test_reaction["count"] == count1_dto.count
        assert test_reaction["reaction"] == count1_dto.reaction
