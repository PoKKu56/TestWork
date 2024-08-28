CREATE TABLE "user"(
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	login VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL
);

CREATE TABLE note(
	id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	text_note text,
	author UUID REFERENCES "user"(id) NOT NULL
);

Insert INTO "user" (login, password) VALUES ('pokku', 'dedpsaf56');