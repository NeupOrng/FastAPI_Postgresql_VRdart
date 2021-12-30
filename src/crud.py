from sqlalchemy.orm import Session

import models, schemas


#players crud
def create_player(player: schemas.PlayerCreate, db: Session):
    db_player = models.Players(username=player.username,oculus_id = player.oculus_id)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(player: schemas.Player, db: Session):
    print(player)
    db.query(models.Players).filter(models.Players.id == player.id).update({'id': player.id, 'username': player.username, 'oculus_id': player.oculus_id, 'highscore': player.highscore, 'fastest_time': player.fastest_time, 'coin': player.coin})
    db.commit()
    return player

def get_player(db: Session, player_id: int):
    return db.query(models.Players).filter(models.Players.id == player_id).first()


def get_all_player(db: Session):
    return db.query(models.Players).filter().all()

def remove_player_record(player_id: int, db: Session):
    #we remove darts record first because darts contain Foreign key of player record
    try:
        db.query(models.Darts).filter(models.Darts.player_id == player_id).delete()
        db.query(models.Players).filter(models.Players.id == player_id).delete()
        db.commit()
        return True
    except:
        return False

#darts crud
def remove_dart_record(dart_id: int, db: Session):
    try:
        db.query(models.Darts).filter(models.Darts.id == dart_id).delete()
        return True
    except:
        return False
