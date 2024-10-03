from django.core.management.base import BaseCommand, CommandError
from blog.models import Post
from django.utils.text import slugify

class Command(BaseCommand):
    """
    Adds new post to the database
    EX:
    $ django-admin add_post --title "exemplo" --content "exemplo"
    """
    help = "creates a new post in the database"

    def add_arguments(self, parser):
        parser.add_argument("--title", type=str, required=True)
        parser.add_argument("--content", type=str, required=True)


    def handle(self, *arg, **options):
        try:
            post= Post.objects.create(
                title= options["title"],
                slug= slugify(options["title"]),
                content=options["content"],
            )
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(self.style.SUCCESS(f"Post ({post.title}) is Created."))

