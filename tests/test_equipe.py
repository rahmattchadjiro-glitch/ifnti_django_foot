import pytest
from tournoi.models import Match
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
       
def test_match_equipe_visiteuse_domicile(db):
    equipe1 = Equipe.objects.create(nom="Equipe A", promo="L1")
    equipe2 = Equipe.objects.create(nom="Equipe B", promo="L2")
    match = Match.objects.create(equipe_visiteuse=equipe2, equipe_domicile=equipe1,date="14/01/20")
    assert match.equipe_visiteuse == equipe2
    assert match.equipe_domicile == equipe1
    assert match.date
    
def test_score_match_non_joue(db):
    equipe1 = Equipe.objects.create(nom="Equipe A", promo="L1")
    equipe2 = Equipe.objects.create(nom="Equipe B", promo="L2")
    match = Match.objects.create(equipe_visiteuse=equipe2, equipe_domicile=equipe1,date="14/01/20", status="EN_ATTENTE")
    assert match.score is None

    