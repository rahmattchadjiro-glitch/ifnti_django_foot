import pytest
#from tournoi.models import Match
from tournoi.models import Equipe

def test_equipe_un_nom_promo(db):
    equipe = Equipe.objects.create(nom="Equipe A", promo="L1")
    assert equipe.nom
    assert equipe.promo 
def test_pas_equipe_avec_meme_nom(db):
    Equipe.objects.create(nom="Equipe A", promo="L1")

    with pytest.raises(Exception):
        Equipe.objects.create(nom="Equipe A", promo="L2")
        
def test_afficher_equipe(db):
    equipe = Equipe.objects.create(nom="Equipe A", promo="L1")
    assert str(equipe) == "Equipe A"   
    
