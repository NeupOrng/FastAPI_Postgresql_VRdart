from sqlalchemy.orm import Session

import models, schemas

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
    print()
    return db.query(models.Players).filter(models.Players.id == player_id).first()


def get_all_player(db: Session):
    return db.query(models.Players).filter().all()
