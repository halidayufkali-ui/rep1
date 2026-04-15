CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO contacts(name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (phone)
    DO UPDATE SET name = EXCLUDED.name;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(names, 1) IS NULL THEN
        RETURN;
    END IF;

    FOR i IN 1..array_length(names, 1) LOOP

        IF phones[i] IS NULL OR length(phones[i]) <> 11 THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];
            CONTINUE;
        END IF;

        INSERT INTO contacts(name, phone)
        VALUES (names[i], phones[i])
        ON CONFLICT (phone) DO UPDATE
        SET name = EXCLUDED.name;

    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts c
    WHERE c.name = p_value OR c.phone = p_value;
END;
$$;