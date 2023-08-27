//Рефакторинг части метода custom_paintscene::mousePressEvent, исходный код внизу файла
//целью рефакторинга было улучшить использование переменной num_clicks_left_button = kol_naj_lkm
//рефакторинг показал, что улучшение невозможно, переменная корректно задана как приватная переменная обработчика mouse event
//найдено два случая присваивания значения объявленной в .h, но неинициализированной переменной


# define LEFT_BUTTON = 1
# define RIGHT_BUTTON = 2
# define TRIANGLE = 1 // ну или какой там тип фигуры 
# define SQUARE = 2
# define CIRCLE = 3
# define PENTAGON = 4
# define COORD_STEP = 1
//num_clicks_left_button = kol_naj_lkm
//shape_type = tip_figury
//current_route = vrem_obj
//current_distance = tek_dist
//num_missiles = tek_prisvaivaemoe_kolvo_raket
//routes_to_target = nabor_atak
//P1_targets = nabor_celey_P1
//P2_targets = nabor_celey_P2
//P1_target_shape = paint_cel_P1
//P2_target_shape = paint_cel_P2
//route_shape = paint_polygon_a
//current_coords = tek_tochki
//current_zzp = vrem_zzp
//paint_zzp = paint_ZZP


void custom_paintscene::mousePressEvent(QGraphicsSceneMouseEvent *event) {
    if (event->button() == LEFT_BUTTON) && (*shape_type == TRIANGLE) && (num_clicks_left_button == 0) {
        first_point = event->scenePos();
        last_point = event->scenePos(); 
        last_point.x() += COORD_STEP; 
        last_point.y() += COORD_STEP; 
        current_route = new route_shape(first_point, last_point);
        this->addItem(current_route);
        num_clicks_left_button = 1;
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == TRIANGLE) && (num_clicks_left_button == 1) && (current_distance > 10.0 ) {
        num_clicks_left_button = 2;
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == TRIANGLE) && (num_clicks_left_button == 1) && (current_distance <= 10.0 ) {
        this->removeItem(current_route);
        num_clicks_left_button = 0;
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == TRIANGLE) && (num_clicks_left_button == 2) {
        bool ok;
        int num_missiles = QInputDialog::getInt(nullptr, tr("Создание носителя"), tr("Количество ракет (более 0, менее 16):"), 5, 1, 15, 1, &ok);
        if (! ok) {num_missiles = 4;}
        num_clicks_left_button = 0;
        current_route->num_missiles = num_missiles  //***ERROR присваивание значения объявленной, но неинициализированной переменной******
        routes_to_target.push_back(current_route)    
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == SQUARE) {
        P1_target_shape *target = new P1_target_shape(event->scenePos());
        P1_targets.push_back(target);
        this->addItem(target);
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == CIRCLE) {
        P2_target_shape *target = new P2_target_shape(event->scenePos());
        P2_targets.push_back(target);
        this->addItem(target);
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == PENTAGON) && (num_clicks_left_button == 0) {
        first_point = event->scenePos();
        last_point = event->scenePos(); 
        last_point.x() += COORD_STEP; 
        last_point.y() += COORD_STEP; 
        QVector<QPointF> current_coords = new QVector(first_point, last_point);
        current_zzp = new paint_zzp(current_coords);
        this->addItem(current_zzp);
        num_clicks_left_button = 1;
    }
    else if (event->button() == LEFT_BUTTON) && (*shape_type == PENTAGON) && (num_clicks_left_button == 1) {
        current_zzp->add_point(event->scenePos()); //***ERROR присваивание значения объявленной, но неинициализированной переменной******
    }
}

//ИСХОДНЫЙ КОД
//РЕФАКТОРИНГ НАЧАЛСЯ ОТСЮДА
void custom_paintscene::mousePressEvent(QGraphicsSceneMouseEvent * event) {

    if (event->button() == 1) {
        if (*tip_figury == 1) {
            if (kol_naj_LKM == 0) {
                first_point = event->scenePos();
                last_point = {event->scenePos().x()+1, event->scenePos().y()+1};
                vrem_obj = new paint_polygon_a(first_point, last_point);
                this->addItem(vrem_obj);
                kol_naj_LKM = 1;
            }
            else if (kol_naj_LKM == 1) {
                if (tek_dist() > 10.0) {
                    kol_naj_LKM = 2;
                }
                else {
                    this->removeItem(vrem_obj);
                    kol_naj_LKM = 0;
                }
            }
            else if (kol_naj_LKM == 2) {
                bool ok;
                int tek_prisvaivaemoe_kolvo_raket = QInputDialog::getInt //
                    (nullptr, tr("Создание носителя"), tr("Количество ракет (более 0, менее 16):"), 5, 1, 15, 1, &ok);
                if (! ok) {
                    tek_prisvaivaemoe_kolvo_raket = 4;
                }
                kol_naj_LKM = 0;
                vrem_obj->kol_raket = tek_prisvaivaemoe_kolvo_raket;
                nabor_atak.push_back(vrem_obj);
            }
        }
        else if (*tip_figury == 2) {
            paint_cel_P1 *cel = new paint_cel_P1(event->scenePos());
            nabor_celey_P1.push_back(cel);
            this->addItem(cel);
//            qDebug() << "кол: " << nabor_celey_P1.size() << endl;
//            qDebug() << cel->center_celi.x() << endl;
        }
        else if (*tip_figury == 3) {
            paint_cel_P2 *cel2 = new paint_cel_P2(event->scenePos());
            nabor_celey_P2.push_back(cel2);
            this->addItem(cel2);
        }
        else if (*tip_figury == 4) {
            if (kol_naj_LKM == 0) {
                QVector<QPointF> tek_tochki = {event->scenePos(), QPointF(event->scenePos().x()+1, event->scenePos().y()+1)};
                vrem_zzp = new paint_ZZP(tek_tochki);
                this->addItem(vrem_zzp);
                kol_naj_LKM = 1;
            }
            else if (kol_naj_LKM == 1) {
                vrem_zzp->add_point(event->scenePos());
            }
        }
    }
//РЕФАКТОРИНГ ЗАКОНЧИЛСЯ ЗДЕСЬ
    else if (event->button() == 2) {
        // qDebug() << "X: " << event->scenePos().x() << "; Y: " << event->scenePos().y() << endl;
        if (kol_naj_LKM == 0) {
            pressed_uni_item = static_cast<QGraphicsObject*>(itemAt(event->scenePos(),QTransform()));
            if (pressed_uni_item != nullptr) {
                //qDebug() << pressed_uni_item->metaObject()->className();
                QString class_of_clicked_object_name = pressed_uni_item->metaObject()->className();
                if (class_of_clicked_object_name == "paint_polygon_a") {
                    for (int i = 0; i < nabor_atak.size(); i++) {
                        if (nabor_atak[i] == pressed_uni_item) {
                            nabor_atak[i]->deleteLater();
                            nabor_atak.remove(i);
                        }
                    }
                }
                else if(class_of_clicked_object_name == "paint_cel_P1") {
                    for (int i = 0; i < nabor_celey_P1.size(); i++) {
                        if (nabor_celey_P1[i] == pressed_uni_item) {
                            nabor_celey_P1[i]->deleteLater();
                            nabor_celey_P1.remove(i);
                        }
                    }
                }
                else if(class_of_clicked_object_name == "paint_cel_P2") {
                    for (int i = 0; i < nabor_celey_P2.size(); i++) {
                        if (nabor_celey_P2[i] == pressed_uni_item) {
                            nabor_celey_P2[i]->deleteLater();
                            nabor_celey_P2.remove(i);
                        }
                    }
                }
                else if(class_of_clicked_object_name == "paint_ZZP") {
                    for (int i = 0; i < nabor_ZZP.size(); i++) {
                        if (nabor_ZZP[i] == pressed_uni_item) {
                            nabor_ZZP[i]->deleteLater();
                            nabor_ZZP.remove(i);
                        }
                    }
                }
            }
            //qDebug() << QString::number(nabor_atak.size());
        }
        else if (*tip_figury == 4 && kol_naj_LKM == 1) {
            nabor_ZZP.push_back(vrem_zzp);
            //this->removeItem(vrem_zzp);
            kol_naj_LKM = 0;
        }
    }
}