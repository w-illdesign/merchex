# admin.py
from django.contrib import admin
from .models import Band, Listing
from django.templatetags.static import static


# -----------------------------
# Configuration de l'admin pour Band
# -----------------------------
class BandAdmin(admin.ModelAdmin):
    """
    Configuration d'affichage et de gestion du modèle Band
    dans l'interface d'administration Django.
    """

    # 🔹 Colonnes affichées dans la liste des groupes
    list_display = ('id', 'name', 'year_formed', 'genre')

    # 🔹 Ajout de filtres latéraux pour faciliter la recherche
    list_filter = ('genre', 'year_formed')

    # 🔹 Champ de recherche rapide (en haut à droite)
    search_fields = ('name',)

    # 🔹 Ordre de tri par défaut (A → Z)
    ordering = ('name',)

    # 🔹 Nombre d’éléments par page dans la liste
    list_per_page = 20


# -----------------------------
# Configuration de l'admin pour Listing
# -----------------------------
class ListingAdmin(admin.ModelAdmin):
    """
    Configuration d'affichage et de gestion du modèle Listing.
    """

    # 🔹 Colonnes visibles dans la liste principale
    list_display = ('id', 'title', 'sold', 'type', 'year', 'band')

    # 🔹 Filtres latéraux pour un tri rapide
    list_filter = ('sold', 'year', 'type', 'band')

    # 🔹 Barre de recherche dans la page admin
    search_fields = ('title',)

    # 🔹 Tri par défaut (du plus récent au plus ancien)
    ordering = ('-year',)

    # 🔹 Permet de modifier un champ directement dans la liste (gain de temps)
    list_editable = ('sold',)

    # 🔹 Limite le nombre d'éléments affichés par page
    list_per_page = 20

    # -----------------------------
    # 🔹 Action personnalisée
    # -----------------------------
    @admin.action(description="Marquer comme vendu")
    def mark_as_sold(self, request, queryset):
        """
        Action pour mettre à jour plusieurs éléments sélectionnés
        et les marquer comme vendus d’un seul clic.
        """
        queryset.update(sold=True)

    # 🔹 Liste des actions disponibles dans le menu déroulant
    actions = ['mark_as_sold']

# -----------------------------
# Configuration de l'admin pour Listing
# -----------------------------
class ThemeAdmin(admin.ModelAdmin):


    # 🔹 Colonnes visibles dans la liste principale
    list_display = ('id', 'theme')


    # -----------------------------
    # 🔹 Action personnalisée
    # -----------------------------
    @admin.action(description="Marquer comme vendu")
    def select_theme(self, request, queryset):
        """
        Action pour mettre à jour plusieurs éléments sélectionnés
        et les marquer comme vendus d’un seul clic.
        """
        queryset.update(theme=True)

    # 🔹 Liste des actions disponibles dans le menu déroulant
    actions = ['mark_as_sold']

# Ajout du CSS personnalisé
class CustomAdmin(admin.AdminSite):
    class Media:
        css = {
            'all': ('custom_admin.css',)
        }

admin.site = CustomAdmin()
# -----------------------------
# Enregistrement des modèles dans l'administration
# ----------’
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)


# -----------------------------
# Personnalisation de l'interface globale
# -----------------------------
# Ces lignes changent les titres visibles dans l'interface d'administration
admin.site.site_header = "Gestion de HELLO DJANGO"         # Titre en haut de la page
admin.site.site_title = "Admin | Label"             # Titre dans l’onglet du navigateur
admin.site.index_title = "Tableau de bord principal" # Titre de la page d’accueil admin

