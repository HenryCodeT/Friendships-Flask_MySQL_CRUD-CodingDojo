-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema friendships_1
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `friendships_1` ;

-- -----------------------------------------------------
-- Schema friendships_1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendships_1` DEFAULT CHARACTER SET utf8 ;
USE `friendships_1` ;

-- -----------------------------------------------------
-- Table `friendships_1`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `friendships_1`.`users` ;

CREATE TABLE IF NOT EXISTS `friendships_1`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendships_1`.`friendships`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `friendships_1`.`friendships` ;

CREATE TABLE IF NOT EXISTS `friendships_1`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  INDEX `fk_friendships_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_friendships_users1_idx` (`friend_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_friendships_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendships_1`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_friendships_users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `friendships_1`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
