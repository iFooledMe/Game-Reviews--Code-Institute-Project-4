from django.db import models
from games.models import Game


# region R E I E W  M O D E L ===============================================|

# region ==== SUB-CLASSES REVIEW ============================================|
class ReviewSite(models.Model):
    site_name = models.CharField(max_length=50)
    site_short_name = models.CharField(max_length=50)
    site_url = models.URLField(max_length=255, null=True, blank=True)
    site_url_name = models.CharField(max_length=50, null=True, blank=True)
    logo_img = models.ImageField(
        upload_to='review_sites/logo_images/',
        max_length=255, null=True, blank=True)
    show_logo_img = models.BooleanField(default=False)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_logo_icon = models.BooleanField(default=False)
    max_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.site_name

# endregion
# ===========================================================================|


class Review(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    review_site = models.ForeignKey(
        ReviewSite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    review_date = models.DateField(null=True, blank=True)
    review_url = models.URLField(max_length=255, null=True, blank=True)
    score = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    max_score = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True)
    short_quote = models.TextField(
        max_length=500, null=True, blank=True)
    long_quote = models.TextField(
        max_length=10000, null=True, blank=True)
    image = models.ImageField(
        upload_to='reviews/review_images/',
        max_length=255, null=True, blank=True)
    show_logo_img = models.BooleanField(default=False)

    def __str__(self):
        show_name = str(self.game) + '_' + str(self.review_site)
        return show_name

# endregion
# ===========================================================================|
