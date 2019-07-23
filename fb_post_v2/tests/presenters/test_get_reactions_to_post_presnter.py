from fb_post_v2.interactors.storages.post_storage import ReactionDetailsDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestGetReactionsToPost:

    def test_get_reactions_to_post(self):
        presenter = JsonPresenter()

        reaction1_dto = ReactionDetailsDTO(user_id=1, username="karthik", profile_pic="", reaction="LIKE")
        reaction2_dto = ReactionDetailsDTO(user_id=2, username="manoj", profile_pic="", reaction="LOVE")
        reaction3_dto = ReactionDetailsDTO(user_id=3, username="bharat", profile_pic="", reaction="HAHA")

        reactions_dto = [reaction1_dto, reaction2_dto, reaction3_dto]

        response = presenter.get_reactions_to_post(reactions_dto=reactions_dto)

        assert len(response["reactions"]) == len(reactions_dto)

        user_ids = [reaction["user_id"] for reaction in response["reactions"]]

        assert reaction1_dto.user_id in user_ids
        assert reaction3_dto.user_id in user_ids

        test_reaction = {}
        for reaction in response["reactions"]:
            if reaction["user_id"] == reaction2_dto.user_id:
                test_reaction = reaction

        assert test_reaction["reaction"] == reaction2_dto.reaction
