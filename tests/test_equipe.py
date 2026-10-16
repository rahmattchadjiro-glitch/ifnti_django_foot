import pytest

from tournoi.models import Equipe

def test_equipe_un_nom_promo(db):
    equipe = Equipe.objects.create(nom="Equipe A", promo="L1")
    assert equipe.nom
    assert equipe.promo 
def test_pas_equipe_avec_meme_nom():
    Equipe.objects.create(nom="Equipe A", promo="L1")

    with pytest.raises(Exception):
        Equipe.objects.create(nom="Equipe A", promo="L2")
        
def test_afficher_equipe():
    equipe = Equipe.objects.create(nom="Equipe A", promo="L1")
    assert str(equipe) == "Equipe A"   
    
def test_match_equipe_visiteuse_receptioniste():
    equipe1 = Equipe.objects.create(nom="Equipe A", promo="L1")
    equipe2 = Equipe.objects.create(nom="Equipe B", promo="L2")
    match = equipe1.matchs.create(equipe_visiteuse=equipe2)
    assert match.equipe_visiteuse == equipe2
    assert match.equipe_receptioniste == equipe1