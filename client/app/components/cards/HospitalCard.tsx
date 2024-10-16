import { HOSPITAL_DATA } from "~/constant";

export default function HospitalCard() {
  return (
    <section className="grid 2xl:grid-cols-5 lg:grid-cols-4 md:grid-cols-2 place-content-center gap-5">
      {HOSPITAL_DATA.map((hospital) => (
        <a
          href={`/hospital/${hospital.nama.toLowerCase().replace(" ", "-")}`}
          key={hospital.nama}
          className="cursor-pointer hover:bg-slate-200 p-4 rounded-md transition-all"
        >
          <img src="/hospital.jpg" alt="hospital" className="w-[300px] rounded-md" />
          <div className="mt-2">
            <h1>{hospital.nama}</h1>
            <h1>{hospital.alamat}</h1>
          </div>
        </a>
      ))}
    </section>
  );
}
