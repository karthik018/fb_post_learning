from .models import User, Post, CommentReaction, Comment, PostReaction
from django.utils import timezone as t
from django.db.models import Q, F, Count
from django.core.exceptions import SuspiciousOperation


def get_user_data(obj):
    user = {
        "userid": obj.user_id,
        "username": obj.user.username,
        "profile_pic": obj.user.profile_pic
    }
    return user


def get_comment_data(comment):
    data = {
        "comment_id": comment['id'],
        "commenter": {
            "userid": comment['user_id'],
            "username": comment['user__username'],
            "profile_pic": comment['user__profile_pic']
        },
        "comment_create_date": comment['comment_create_date'].strftime("%Y-%m-%d %H:%M:%S"),
        "comment_message": comment['message']
    }
    return data


def get_reply_data(reply):
    replied_at = reply.comment_create_date.strftime("%Y-%m-%d %H:%M:%S")
    reply_data = {
        "comment_id": reply.id,
        "commenter": get_user_data(reply),
        "comment_create_date": replied_at,
        "comment_message": reply.message
    }
    return reply_data


def get_post(post_id):
    print(post_id)
    post = Post.objects.select_related('user').get(id=post_id)
    posted_by = get_user_data(post)
    posted_at = post.post_create_date.strftime("%Y-%m-%d %H:%M:%S")
    post_content = post.post_description
    post_reactions = PostReaction.objects.filter(post_id=post_id).values('reaction')
    reactions = []
    for reaction in post_reactions:
        reactions.append(reaction['reaction'])
    post_reaction_count = len(reactions)
    # post_reactions = list(set(reactions))
    post_reactions = list(post_reactions)

    post_comments = Comment.objects.filter(post_id=post_id, commented_on_id=None).values('id', 'user_id',
                                                                                         'user__username',
                                                                                         'user__profile_pic',
                                                                                         'commented_on_id',
                                                                                         'comment_create_date',
                                                                                         'message')
    comments_ids = [comment['id'] for comment in post_comments]

    replies = Comment.objects.filter(commented_on_id__in=comments_ids).values('id', 'user_id',
                                                                              'user__username',
                                                                              'user__profile_pic',
                                                                              'commented_on_id',
                                                                              'comment_create_date',
                                                                              'message')
    comments_ids[len(comments_ids) + 1:] = [reply['id'] for reply in replies]

    comment_reactions = CommentReaction.objects.filter(comment_id__in=comments_ids).values('comment_id', 'reaction')

    comment_reaction = {}
    for react in comment_reactions:
        l = []
        r = react['reaction']
        l.append(react)
        try:
            comment_reaction[react['comment_id']].append(react)

        except:
            comment_reaction[react['comment_id']] = l

    for id in comment_reaction:
        count = len(comment_reaction[id])
        # reactions = list(set(comment_reaction[id]))
        data = {"count": count, "types": comment_reaction[id]}
        comment_reaction[id] = data

    comment_replies = {}
    for reply in replies:
        comment_reply = []
        d = get_comment_data(reply)
        try:
            d["reactions"] = comment_reaction[reply['id']]
        except:
            d["reactions"] = {"count": 0, "types": []}
        comment_reply.append(d)
        try:
            comment_replies[reply['commented_on_id']].append(d)
        except:
            comment_replies[reply['commented_on_id']] = comment_reply

    comments = []
    for comment in post_comments:
        d = get_comment_data(comment)
        try:
            d["reactions"] = comment_reaction[comment['id']]
            d["replies_count"] = len(comment_replies[comment['id']])
            d["replies"] = comment_replies[comment['id']]
        except:
            d['reaction'] = {"count": 0, "types": []}
            d['replies_count'] = 0
            d['replies'] = []
        comments.append(d)

    result = {"postid": post_id, "posted_by": posted_by, "post_create_date": posted_at, "post_content": post_content,
              "reactions": {
                  "count": post_reaction_count,
                  "types": post_reactions
              }, "comments": comments, "comment_count": len(comments)}
    return result


def create_post(user_id, post_content):
    print(user_id, post_content)
    post = Post(user_id=user_id, post_description=post_content, post_create_date=t.now())
    post.save()
    return post.id


def add_comment(post_id, comment_user_id, comment_text):
    comment = Comment(post_id=post_id, user_id=comment_user_id, comment_create_date=t.now(), message=comment_text)
    comment.save()
    return comment.id


def reply_to_comment(comment_id, reply_user_id, reply_text):
    comment = Comment.objects.get(id=comment_id)
    comment_on_id = comment.commented_on_id
    if comment_on_id is not None:
        comment = Comment.objects.get(id=comment.commented_on_id.id)
    reply = Comment(post_id=comment.post_id, user_id=reply_user_id, commented_on_id=comment,
                    comment_create_date=t.now(),
                    message=reply_text)
    reply.save()
    return reply.id


def react_to_post(user_id, post_id, reaction_type):
    try:
        react = PostReaction.objects.get(user_id=user_id, post_id=post_id)
        if react.reaction == reaction_type:
            react.delete()
            return react.id
        else:
            reaction_type = reaction_type
            react.reaction = reaction_type
            react.save()
            return react.id
    except:
        react = PostReaction(user_id=user_id, post_id=post_id, reaction=reaction_type)
        react.save()
        return react.id


def react_to_comment(user_id, comment_id, reaction_type):
    try:
        react = CommentReaction.objects.get(user_id=user_id, comment_id=comment_id)
        if react.reaction == reaction_type:
            react.delete()
            return react.id
        else:
            reaction_type = reaction_type
            react.reaction = reaction_type
            react.save()
            return react.id
    except:
        react = CommentReaction(user_id=user_id, comment_id=comment_id, reaction=reaction_type)
        react.save()
        return react.id


def get_user_posts(user_id, offset, limit):
    posts = Post.objects.filter(user_id=user_id)
    posts_list = [post.id for post in posts]
    return posts_list[offset: offset+limit]


def get_posts_with_more_positive_reactions():
    positive_posts = PostReaction.objects.values('post').annotate(
        positive_count=Count('reaction', filter=Q(reaction__in=("LIKE", "LOVE", "WOW", "HAHA"))),
        negative_count=Count('reaction', filter=Q(reaction__in=("SAD", "ANGRY")))).filter(
        positive_count__gt=F('negative_count')).values('post_id')
    positive_posts = [{'postid': post['post_id']} for post in positive_posts]
    return list(positive_posts)


def get_posts_reacted_by_user(user_id):
    likes = PostReaction.objects.filter(user_id=user_id)
    posts_list = [get_post(like.post.id) for like in likes]
    return posts_list


def get_reactions_to_post(post_id, offset, limit):
    likes = PostReaction.objects.select_related('user').filter(post_id=post_id)
    reactions = []
    for like in likes:
        post_reactions = get_user_data(like)
        post_reactions["reaction"] = like.reaction
        reactions.append(post_reactions)
    return reactions[offset: offset+limit]


def get_reaction_metrics(post_id):
    likes = PostReaction.objects.filter(post_id=post_id).values('reaction').annotate(react_count=Count('reaction'))
    # reaction_count = {like['reaction']: like['react_count'] for like in likes}
    reaction_metrics = [{"count": like['react_count'], "reaction": like['reaction']} for like in likes]
    return reaction_metrics


def get_total_reaction_count():
    reaction_count = PostReaction.objects.all().count()
    return reaction_count


def get_replies_for_comment(comment_id, offset, limit):
    comment = Comment.objects.get(id=comment_id)
    if comment.commented_on_id is not None:
        raise SuspiciousOperation
    replies = Comment.objects.select_related('user').filter(commented_on_id=comment_id)[offset: offset+limit]
    comment_replies = [get_reply_data(reply) for reply in replies]

    return comment_replies


def delete_post(post_id):
    try:
        Post.objects.get(id=post_id).delete()
    except:
        raise Post.DoesNotExist
